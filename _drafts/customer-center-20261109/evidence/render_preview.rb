# A limited local Markdown preview using macOS bundled RDoc, not Jekyll/kramdown.
require 'json'
require 'rdoc'
require 'rdoc/markdown'
require 'rdoc/markup/to_html'
require 'cgi'
base=File.dirname(__FILE__)
items=JSON.parse(File.read(File.join(base,'preview-input.json')))
options=RDoc::Options.new
items.each do |item|
  item['html']=RDoc::Markdown.parse(item['markdown']).accept(RDoc::Markup::ToHtml.new(options))
  raise "Missing paragraph #{item['locale']}" unless item['html'].include?('<p>')
  raise "Leaked Markdown #{item['locale']}" if item['html'].include?('###')
end
sets=items.each_slice(4).to_a
sets << items.select { |i| ['ar','he','de','support'].include?(i['locale']) }
sets.each_with_index do |group,index|
  large=index==sets.length-1
  cards=group.map do |i|
    "<article data-locale='#{i['locale']}'><header>#{i['locale']} · #{large ? '24px' : '16px'} · limited RDoc preview</header><main dir='#{i['dir']}'>#{i['html']}</main></article>"
  end.join
  js=<<~JS
    const cards=[...document.querySelectorAll('article')].map(a=>({locale:a.dataset.locale,outerWidth:a.getBoundingClientRect().width,width:a.clientWidth,scrollWidth:a.scrollWidth,height:a.scrollHeight,paragraphs:a.querySelectorAll('p').length,dir:a.querySelector('main').dir,visible:a.querySelector('p').getBoundingClientRect().height>0}));
    document.getElementById('metrics').textContent=JSON.stringify({renderer:'RDoc + Chrome; NOT Jekyll',font:#{large ? 24 : 16},cards});
  JS
  document="<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><style>html,body{margin:0;background:white;color:#222;font-family:Arial,sans-serif}body{display:flex;align-items:flex-start}article{width:320px;box-sizing:border-box;padding:16px;border-right:1px solid #ccc;flex-shrink:0}header{font-size:12px;color:#555;margin-bottom:16px}main{font-size:#{large ? 24 : 16}px;line-height:1.5}h3{font-size:1.15em}h3 span{display:none}p{margin:0 0 1em}#metrics{display:none}</style></head><body>#{cards}<pre id='metrics'></pre><script>#{js}</script></body></html>"
  File.write(File.join(base,"preview-#{index+1}.html"),document)
end
puts "Rendered #{items.length} changed sections with RDoc; #{sets.length} preview sheets (9 standard, 1 large)."
