# Feature detector

Thần kinh học đã chứng minh được rằng những điểm ở các góc cạnh của một bức ảnh thường sẽ gây chú ý hơn. Chẳng hạn khi nhìn vào một khuôn mặt người, bộ não thường lưu lại các đặc trưng về các góc cạnh của khóe mắt, khóe miệng, mũi,..

<img src="http://www.arcsoft.com/resource/image/technology/face/face-outline.jpg" alt="Credit: http://www.arcsoft.com/" style="width: 10px; height: 10px"/>

Tận dụng lý thuyết đó, trong xử lý ảnh và thị giác máy, người ta thường lấy ra các điểm góc của một object để làm đặc trưng nhân dạng.

Có nhiều phương pháp nhận diện góc (corner detection) như:
- Harris
- SIFT
- SUFT

Trong bài đọc này chúng ta cùng tìm hiểu về 2 phương pháp đầu tiên là Harris và SIFT

## Harris Corner Detection

## SIFT (Scaled-Invariant Feature Transform)
Harris là phương pháp có thể nhận dạng được góc cho dù có rotate bức ảnh (cũng dễ hiểu thôi vì có rotate thì corner vẫn là corner). Nhưng nếu scaled bức ảnh thì sao? Phương pháp của Harris bắt đầu tỏ ra không hiệu quả và đa phần là không nhận diện được corner của cùng một bức ảnh khi bị scaled

Để khác phục tình trạng đó, một thuật toán khác là SIFT ra đời.

### Scale-space Extrema Detection
Ở trong Harris, việc chọn window size là cố định, do đó, khi ảnh bị scaled bigger thì window size sẽ không thể cover được corner nữa. Ý tưởng chính của SIFT là sử dụng phương pháp gọi là **scaled-space** để chọn ra size của window sao cho phù hợp nhất.

**Scaled-space** sử dụng phương pháp Laplacian of Gaussian để với mỗi một điểm ảnh (x,y) ta chọn ra được một số gọi là \sigma để tìm ra được size phù hợp cho window. The bigger sigma, the bigger window size, and vice versa.



