fitting by PyROOT
===

PyROOTでフィッテイングするだけ(≠rootpy)
枠組みができたからあげる

間違いなく忘れているであろう将来の自分へ
---
ROOTでフィッテイングを実行し、結果が得られるのは事実。多くの関数で結果を出せる。
ただし多くのサンプルコードが手続き的であり触りづらいのも事実。
よって、python でまとめて作った。第１目的は、ipython にてインタラクティブに開発したかった。今日は１次関数(pol1)でフィッテイングに成功しているが、これは ROOT のドキュメントを見ればオプションの選択肢はわかる。

[フィッテイングの解説、オプションについて](http://www.dw-sapporo.co.jp/technology/658766f830d530a130a430eb7f6e304d5834/root_usersguide_jp/5FittingHistgram.pdf)

これは、python3 で動いている。 2015年4月23日
ROOT をインストールした後に、シェルの環境変数 $PYTHONPATH に ROOTの python distribution の場所を追加すれば、import ROOT には成功するので、このコードは動く。

```
$ brew install root
```