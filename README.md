# mastermind
*A simple Mastermind game with a GUI // Grafiksel kullanıcı arayüzüne sahip basit bir Mastermind oyunu*

[Wikipedia link for description of the game](https://en.wikipedia.org/wiki/Mastermind_(board_game))

## Mastermind nasıl bir oyun?

Mastermind, 1970’lerin başında Mordecai Meirowitz tarafından geliştirilmiş, karşılıklı iki kişiyle oynanan bir masa oyunudur. <br/>
Oyunculardan ilki kod yapıcı (codemaker) olarak adlandırılır ve görevi 6 elemanlı bir renk kümesinden 4 adet renk seçip, diğer oyuncudan çözmesini bekleyeceği gizli bir renk kombinasyonu oluşturmaktır. <br/>
İkinci oyuncu ise kod kırıcı (codebreaker) olarak adlandırılır ve amacı ilk oyuncunun oluşturduğu renk kombinasyonunu en fazla 13 aşamada bulmaktır. <br/>
İlk oyuncu 6’lık bir kümeden diğer oyuncunun görmeyeceği şekilde 4 farklı renkte boncuk(color peg) seçip gizli bölmeye dizer. <br/>
Daha sonra kod kırıcı, rastgele bir tahminde bulunur. <br/>
Tahmin neticesinde, gizli kombinasyona göre renk olarak doğru fakat yer olarak yanlış her boncuk için beyaz çivi, hem renk hem de yer olarak doğru olan her boncuk için ise siyah çivi yerleştirilir. <br/>
Siyah ve beyaz çiviler çözüm kümesini kısıtlayarak kodu çözmeye çalışan oyuncuyu doğru cevaba yönlendirir. <br/>
Oyunun amacı en fazla 13 tahminde doğru cevaba ulaşmaktır. <br/>

## Masaüstü versiyonu nasıl?

Bu program 6 farklı renk içeren bir renk kümesinden rastgele 4 renk seçer. Seçilen renk kombinasyonunda bir renk en fazla iki kez kullanılmıştır. <br/>
Renkler: (*r*)ed, (*g*)reen, (*b*)lue, (*m*)agenta, (*c*)yan, (*y*)ellow <br/>
Oyuncu, ekrana renklerin baş harflerini girerek bir tahminde bulunur. <br/>
Tahmin neticesinde, gizli kombinasyona göre renk olarak doğru fakat yer olarak yanlış her boncuk için beyaz, hem renk hem de yer olarak doğru olan her boncuk için ise siyah çivi yerleştirilir. <br/>
Bu program; oyuncunun girdiği renk sayısını ve renk bilgisini kontrol ederek oyuncuya bilgi vermektedir. <br/>
Bu programın kullanıcı arayüzü (GUI), tkinter kullanarak tasarlanmıştır. <br/>
