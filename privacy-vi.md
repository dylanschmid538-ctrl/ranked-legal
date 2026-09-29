---
title: Chính sách quyền riêng tư · Calisthenics Skills – Ranked
permalink: /privacy/vi/
---

> Đây là bản dịch. Nếu có khác biệt, [bản tiếng Anh](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/) được ưu tiên áp dụng.

# Chính sách quyền riêng tư · Calisthenics Skills – Ranked

**Cập nhật lần cuối: ngày 29 tháng 9 năm 2026**

Chính sách này mô tả Ranked thu thập dữ liệu gì, dữ liệu được gửi đến đâu và bạn có thể làm gì. Nội dung được viết dựa trên mã thực tế của ứng dụng, không theo mẫu; nếu có điều gì không đúng, cần kiểm tra mã ứng dụng.

Ranked do **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Thụy Sĩ** vận hành; liên hệ **dylan.schmid538@gmail.com**. Bà là bên kiểm soát việc xử lý dữ liệu được mô tả ở đây.

---

## 1. Tóm tắt

Ranked **không có tài khoản người dùng hay máy chủ riêng**. Mọi thông tin về việc tập luyện của bạn — từng hiệp được ghi lại, tiến độ của từng kỹ năng, thứ hạng, Power Level và bản đồ cơ thể — đều được lưu trên điện thoại và không được tải lên nơi nào.

**Tuổi, giới tính, chiều cao và cân nặng của bạn không bao giờ rời khỏi thiết bị.** Công thức xếp hạng sử dụng các thông tin này trên điện thoại. Chúng không được gửi cho chúng tôi hay dịch vụ phân tích.

Chỉ có hai loại dữ liệu rời khỏi thiết bị:

1. **Thống kê sử dụng ẩn danh**, giúp chúng tôi biết ứng dụng được dùng như thế nào. Bạn có thể tắt trong ứng dụng bất kỳ lúc nào.
2. **Dữ liệu mua hàng**, để xác minh gói đăng ký App Store. Apple xử lý thanh toán; chúng tôi không bao giờ thấy thông tin thanh toán của bạn.

Ranked không theo dõi bạn giữa các ứng dụng hoặc trang web khác, không hiển thị quảng cáo và không đọc dữ liệu từ Apple Health.

---

## 2. Dữ liệu ở lại trên thiết bị

Những thông tin sau được lưu trong cơ sở dữ liệu riêng của ứng dụng trên điện thoại và không bao giờ được truyền đi:

- Mọi buổi tập, hiệp, lần lặp, thời gian giữ và mức tạ bổ sung mà bạn ghi lại
- Tiến độ từng kỹ năng và giai đoạn, lịch sử thứ hạng và Power Level
- Kế hoạch, lịch tập, lời nhắc và tùy chọn của bạn
- Các số đo cơ thể bạn đã nhập (tuổi, giới tính, chiều cao, cân nặng)
- Ghi chú tập luyện

Ứng dụng không loại cơ sở dữ liệu này khỏi bản sao lưu của thiết bị. Nếu bạn dùng iCloud Backup hoặc sao lưu trên máy tính, dữ liệu tập luyện sẽ nằm trong bản sao lưu và trở lại khi khôi phục — theo điều khoản của Apple, không phải của chúng tôi.

Xóa ứng dụng sẽ xóa toàn bộ dữ liệu này khỏi thiết bị. Chúng tôi không thể khôi phục vì chưa từng sở hữu dữ liệu đó.

---

## 3. Dữ liệu rời khỏi thiết bị

### 3.1 Thống kê sử dụng (PostHog)

Chúng tôi sử dụng **PostHog**, được lưu trữ tại **Liên minh Châu Âu**, để hiểu cách ứng dụng được sử dụng. Ứng dụng gửi một danh sách sự kiện cố định:

- bạn đã đến, hoàn tất hoặc quay lại từ bước thiết lập nào, cùng thời gian thực hiện từng bước;
- kết quả đánh giá ban đầu: số nhánh kỹ năng và giai đoạn bạn đánh dấu đã đạt, kỹ năng bạn chọn làm mục tiêu, thứ hạng ban đầu và thứ hạng của từng vùng trong sáu vùng cơ thể;
- thời điểm màn hình mua hàng được hiển thị hoặc đóng và thời điểm giao dịch mua được bắt đầu, hoàn tất hoặc khôi phục, cùng sản phẩm và ưu đãi liên quan; thời điểm sau đó ứng dụng nhận thấy một giai đoạn dùng thử hoặc đăng ký trả phí đang hoạt động, cùng sản phẩm và thông tin đây có phải giao dịch thử nghiệm hay không (đây không phải bản ghi của mọi lần thu phí và không được gửi khi ứng dụng đóng);
- thời điểm thứ hạng của bạn thay đổi và kỹ năng gây ra thay đổi đó;
- thời điểm bạn hoàn thành một giai đoạn: kỹ năng và giai đoạn nào, và kết quả đó đến từ một hiệp đã ghi, một buổi tập được bổ sung sau hoặc một xác nhận thủ công;
- những màn hình bạn mở và thời điểm kết thúc buổi tập. Sự kiện kết thúc buổi tập không có chi tiết: không có bài tập, hiệp tập hay con số.

Phần mềm PostHog trong ứng dụng cũng gắn thông tin kỹ thuật tiêu chuẩn vào từng sự kiện, chẳng hạn kiểu máy, phiên bản iOS, phiên bản ứng dụng, ngôn ngữ và múi giờ, đồng thời ghi nhận khi ứng dụng mở hoặc chuyển sang nền. Như mọi dịch vụ internet, PostHog nhận địa chỉ IP của yêu cầu; từ đó có thể suy ra vị trí gần đúng (quốc gia hoặc thành phố).

**Những gì không có trong đó:** tên, địa chỉ email (ứng dụng không bao giờ hỏi), mã định danh tài khoản (không có tài khoản), tuổi, giới tính, chiều cao, cân nặng hay nội dung các buổi tập của bạn.

**Cách nhận diện:** PostHog tạo một mã định danh ngẫu nhiên khi ứng dụng chạy lần đầu và lưu trên thiết bị. Tất cả sự kiện được nhóm theo mã này. Ứng dụng không bao giờ cho PostHog biết bạn là ai, và cũng không có tài khoản hay email để cung cấp.

**Cách tắt:** Cài đặt ▸ Quyền riêng tư ▸ *Chia sẻ dữ liệu sử dụng ẩn danh*. Khi tắt, ứng dụng ngừng gửi sự kiện kể từ thời điểm đó. Cài đặt được lưu trên thiết bị và vẫn giữ nguyên sau khi cập nhật ứng dụng.

### 3.2 Phân bổ nguồn từ Apple Search Ads

Nếu bạn cài Ranked sau khi nhấn một quảng cáo Apple Search Ads, khi khởi chạy lần đầu ứng dụng sẽ hỏi Apple một lần về nguồn cài đặt. Apple trả về chiến dịch, nhóm quảng cáo, từ khóa và bộ nội dung sáng tạo của quảng cáo đó, quốc gia hoặc khu vực và ngày nhấn, cùng thông tin đây là lần tải mới hay tải lại. Ứng dụng gắn các giá trị này với mã PostHog ẩn danh mô tả ở §3.1 để các sự kiện sau đó có thể được nhóm theo quảng cáo đã đưa bạn đến ứng dụng.

Việc này dùng bộ công cụ **AdServices** của Apple, không sử dụng mã định danh quảng cáo (IDFA) và Apple không coi đó là theo dõi; vì vậy không có hộp thoại xin phép theo dõi. Nếu bạn không đến từ quảng cáo, Apple cho biết điều đó và không có dữ liệu nào khác được gắn vào. Tắt thống kê sử dụng (§3.1) cũng dừng hoạt động này.

### 3.3 Mua hàng (Apple và RevenueCat)

Gói đăng ký được **Apple** bán và tính phí qua App Store. Chúng tôi không bao giờ thấy thông tin thanh toán, Tài khoản Apple hay tên của bạn.

Ứng dụng dùng **RevenueCat** để kiểm tra gói đăng ký có đang hoạt động hay không. RevenueCat nhận hồ sơ mua gói đăng ký từ App Store — sản phẩm đã mua, thời điểm bắt đầu và hết hạn — cùng thông tin kỹ thuật tiêu chuẩn như phiên bản iOS và ứng dụng. RevenueCat nhận diện lượt cài đặt bằng mã ngẫu nhiên do chính họ tạo và lưu trên thiết bị. Chúng tôi không cung cấp cho RevenueCat tên, email hay thông tin nhận dạng khác; vì Ranked không có tài khoản, không có danh tính nào như vậy để cung cấp.

Khi bạn nhấn **Khôi phục giao dịch mua**, ứng dụng hỏi Apple về các giao dịch được thực hiện bằng Tài khoản Apple đang đăng nhập trên thiết bị và chuyển kết quả cho RevenueCat theo cùng cách.

---

## 4. Những việc Ranked không làm

- **Không có tài khoản.** Bạn không bao giờ phải đăng nhập. Không có hồ sơ của bạn trên máy chủ nào.
- **Không sử dụng Apple Health.** Ranked không đọc hay ghi vào ứng dụng Sức khỏe.
- **Không dùng máy ảnh, ảnh, micrô, vị trí hay danh bạ.** Ứng dụng không yêu cầu những quyền này.
- **Không theo dõi giữa các ứng dụng hoặc trang web**, không dùng mã định danh quảng cáo, không có quảng cáo trong ứng dụng, không bán hoặc cung cấp dữ liệu cho bên môi giới dữ liệu.
- **Không có máy chủ thông báo đẩy.** Lời nhắc được lên lịch ngay trên điện thoại; không có thông tin nào về chúng rời khỏi thiết bị. Bạn được hỏi trước khi lời nhắc đầu tiên được lên lịch và có thể tắt chúng trong Cài đặt iOS bất cứ lúc nào.

---

## 5. Cơ sở pháp lý (GDPR và revDSG của Thụy Sĩ)

| Hoạt động xử lý | Cơ sở |
|---|---|
| Mua hàng và xác minh gói đăng ký (§3.3) | Thực hiện hợp đồng |
| Thống kê sử dụng (§3.1) | Lợi ích chính đáng trong việc hiểu và cải thiện ứng dụng; bạn có thể phản đối bất kỳ lúc nào bằng cách tắt, xem §8 |
| Phân bổ Search Ads (§3.2) | Lợi ích chính đáng trong việc biết quảng cáo nào hiệu quả; cách phản đối như trên |

**Ở đây áp dụng hai luật, không phải một.** Ranked được vận hành từ Thụy Sĩ, vì vậy Đạo luật Liên bang Thụy Sĩ về Bảo vệ Dữ liệu đã sửa đổi (**revDSG**, có hiệu lực từ tháng 9 năm 2023) điều chỉnh việc xử lý này. **GDPR** cũng áp dụng khi ứng dụng được dùng từ Liên minh Châu Âu hoặc Vương quốc Anh. Khi hai luật khác nhau, chúng tôi tuân theo quy định nghiêm ngặt hơn. Cư dân Thụy Sĩ có các quyền cốt lõi tương tự được nêu ở §8 theo Điều 25 và các điều tiếp theo của revDSG.

---

## 6. Nơi xử lý dữ liệu

- **PostHog** xử lý thống kê sử dụng tại Liên minh Châu Âu.
- **RevenueCat, Inc.** có trụ sở tại Hoa Kỳ và xử lý dữ liệu mua hàng mô tả ở §3.3 tại đó.
- **Apple** xử lý giao dịch mua và yêu cầu phân bổ Search Ads theo chính sách quyền riêng tư riêng của Apple, áp dụng cho Tài khoản Apple của bạn độc lập với ứng dụng này.

---

## 7. Thời gian lưu giữ

Thống kê sử dụng được lưu theo thời hạn lưu giữ PostHog áp dụng cho gói dịch vụ của chúng tôi. Chúng tôi không hứa một số tháng cố định vì PostHog không cho phép chúng tôi đặt thời hạn đó; ghi một thời hạn không thể thực hiện trong chính sách còn tệ hơn không ghi.

RevenueCat giữ hồ sơ mua hàng trong khi gói đăng ký và lịch sử của nó còn tồn tại, như việc xác minh gói đăng ký đòi hỏi.

Mọi thứ trên thiết bị vẫn ở đó cho đến khi bạn xóa ứng dụng.

---

## 8. Quyền của bạn

Bạn có thể, bất kỳ lúc nào:

- **Tắt thống kê sử dụng** trong Cài đặt ▸ Quyền riêng tư. Đây là quyền phản đối của bạn và, khi việc xử lý dựa trên sự đồng ý, quyền rút lại sự đồng ý; thay đổi có hiệu lực ngay và không cần nêu lý do.
- **Xóa dữ liệu của mình.** Vì Ranked không giữ thông tin về bạn trên máy chủ, việc xóa ứng dụng sẽ xóa tất cả những gì ứng dụng tự lưu.
- **Yêu cầu chúng tôi xóa hồ sơ phân tích ẩn danh.** Chúng tôi không thể tìm theo tên vì hồ sơ không có tên; nếu bạn gửi ngày gần đúng khi lần đầu dùng ứng dụng và thiết bị đã dùng, chúng tôi sẽ tìm thủ công và xóa.
- **Yêu cầu bản sao** dữ liệu mà dịch vụ lưu dưới mã định danh của bạn, yêu cầu **sửa** hoặc **hạn chế** xử lý trong khi yêu cầu đang được xem xét.
- **Khiếu nại đến cơ quan giám sát** tại quốc gia của bạn; ở Thụy Sĩ là Ủy viên Liên bang về Bảo vệ Dữ liệu và Thông tin (FDPIC).

Hãy viết thư tới **dylan.schmid538@gmail.com** để thực hiện các quyền này.

---

## 9. Trẻ em

Ranked dành cho người **từ 16 tuổi trở lên**. Ứng dụng hỏi tuổi khi thiết lập vì công thức xếp hạng phụ thuộc vào tuổi và không hướng đến người trẻ hơn. Chúng tôi không cố ý thu thập dữ liệu của người dưới 16 tuổi.

---

## 10. Thay đổi

Phiên bản đăng tại địa chỉ này là phiên bản hiện hành; ngày ở đầu trang cho biết lần thay đổi gần nhất. Các phiên bản trước vẫn hiển thị trong lịch sử công khai của kho lưu trữ dùng để xuất bản những trang này để bạn xem điều gì đã thay đổi và khi nào.

---

> **⚠️ Không phải tư vấn pháp lý.** Tài liệu này do kỹ sư soạn từ mã nguồn ứng dụng, không phải luật sư. Tài liệu mô tả chính xác hệ thống vào ngày nêu trên; mỗi khẳng định đã được đối chiếu với dữ liệu ứng dụng thực sự gửi. Tài liệu **chưa** được thẩm định về tuân thủ GDPR, revDSG của Thụy Sĩ, CCPA hay bất kỳ chế độ pháp luật nào khác. Việc xuất bản đáp ứng yêu cầu của Apple nhưng không tự làm cho bạn tuân thủ luật. Hãy nhờ luật sư xem xét khi ứng dụng bắt đầu có doanh thu.
