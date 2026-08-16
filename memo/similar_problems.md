# 類題リンク集

典型を理解した後、同じ考え方を別の問題で再現できるか確認するためのリンク集。

問題の横にあるチェックボックスは、解説を見ずにACできたらチェックする。ABCの番号帯では分けず、考察で使う視点ごとに分類する。

## 寄与・組合せ

多数の選び方を直接走査せず、式を分解して「固定した要素や組が答えに何回現れるか」を数える。

特に組合せが現れそうなら、必ず選ぶ要素を先に固定し、「残り何個から、あと何個選ぶか」を日本語で説明してから `C(n, r)` にする。

### 基礎：各要素・ペアの寄与を数える

- [ ] [ABC437 D - Sum of Differences](https://atcoder.jp/contests/abc437/tasks/abc437_d)
  - 2数の差の絶対値を、大小関係を固定して各要素の寄与として数える。
  - 寄与の基礎を確認する。ABC471 Eよりかなり軽め。

- [ ] [ABC353 D - Another Sigma Problem](https://atcoder.jp/contests/abc353/tasks/abc353_d)
  - 2数を連結した値を項ごとに分解し、各要素が左右で何回使われるかを数える。

- [ ] [ABC318 E - Sandwiches](https://atcoder.jp/contests/abc318/tasks/abc318_e)
  - 中央の位置を固定し、左右にある同じ値の組数を数える。
  - 固定位置を一つ動かしたときの変化だけを更新する、右端固定・DP的な見方もできる。

- [ ] [ABC308 E - MEX](https://atcoder.jp/contests/abc308/tasks/abc308_e)
  - 3要素の中央を固定し、左右の値ごとの個数からその項の寄与を数える。
  - 値の種類数が少ない場合の寄与集計を練習する。

### 区間に含まれる回数を数える

- [ ] [ABC371 E - I Hate Sigma Problems](https://atcoder.jp/contests/abc371/tasks/abc371_e)
  - 各要素が区間内の種類数を1増やす範囲を、同じ値の直前の出現位置から数える。
  - 全区間を列挙せず、各位置が新しい種類として寄与する区間数を加える。

- [ ] [ABC468 E - Average of Subarrays](https://atcoder.jp/contests/abc468/tasks/abc468_e)
  - 各要素を固定し、長さごとにその要素を含む区間数を数えて、全区間の平均への寄与を求める。
  - 区間数が台形になることと、右端固定で前の状態から差分更新する見方の両方を確認する。

- [ ] [ABC423 E - Sum of Subarrays](https://atcoder.jp/contests/abc423/tasks/abc423_e)
  - 各クエリの範囲内にある全区間の和を、各要素が含まれる区間数の寄与へ分解する。
  - 「左端の選び方 × 右端の選び方」を式にし、クエリごとに高速計算できるよう前計算する。

- [ ] [ABC390 F - Double Sum 3](https://atcoder.jp/contests/abc390/tasks/abc390_f)
  - 全区間の操作回数の和を、各値が1回の操作を必要とさせる区間数の寄与として数える。

- [ ] [ABC173 F - Intervals on Tree](https://atcoder.jp/contests/abc173/tasks/abc173_f)
  - 連結成分数をより単純な量へ分解し、各頂点と各辺が含まれる区間数を数える。
  - `Comb` は使わないが、複雑な答えを局所的な寄与へ分解する練習にする。

### 組合せで登場回数を数える

- [ ] [ABC471 E - Sum of Square of Sum](https://atcoder.jp/contests/abc471/tasks/abc471_e)
  - 1要素の2乗項と、異なる2要素の積の項に展開し、それぞれが選ばれる回数を `Comb` で数える。

- [ ] [ABC151 E - Max-Min Sums](https://atcoder.jp/contests/abc151/tasks/abc151_e)
  - 要素を一つ固定し、その要素が最小値または最大値になる選び方を数える。
  - 固定した要素以外をどの範囲から選ぶかを整理し、`Comb` の式に確証を持つ練習にする。

- [ ] [ABC127 E - Cell Distance](https://atcoder.jp/contests/abc127/tasks/abc127_e)
  - 2マスを固定し、その組が含まれる `K` マスの選び方を数える。
  - ABC471 Eのペア項と同じ寄与に加え、二次元の距離の総和をまとめる。

- [ ] [ABC221 E - LEQ](https://atcoder.jp/contests/abc221/tasks/abc221_e)
  - 部分列の両端を固定し、その内側にある要素の選び方を数える。
  - 寄与の式と、条件を満たす過去の要素を集計するデータ構造を組み合わせる。

- [ ] [ABC169 F - Knapsack for All Subsets](https://atcoder.jp/contests/abc169/tasks/abc169_f)
  - 集合とその部分集合という二重の選び方を、各要素の少数の状態へ分解する。
  - 巨大な全列挙を、要素ごとの選択とDPへ反転する応用問題。

### 仕切り・隙間への分配を数える

- [ ] [ABC110 D - Factorization](https://atcoder.jp/contests/abc110/tasks/abc110_d)
  - `M` を素因数分解し、各素因数の指数を `N` 個の整数へ0個以上ずつ分配する。
  - 重複組合せによる分配の基礎を確認する。

- [ ] [ABC132 D - Blue and Red Balls](https://atcoder.jp/contests/abc132/tasks/abc132_d)
  - 青いボールの連続ブロック数を固定する。
  - 青いボールを空でないブロックへ分配し、赤いボールが作る隙間から置き場所を選ぶ。
  - ABC458 Eの直前練習として特におすすめ。

- [ ] [ABC156 E - Roaming](https://atcoder.jp/contests/abc156/tasks/abc156_e)
  - 空になった部屋数を固定し、空にする部屋の選択と、余った人の分配を `Comb` で数える。
  - 問題文から「同じものを箱へ分配する問題」へ言い換える練習にする。

- [ ] [ABC405 E - Fruit Lineup](https://atcoder.jp/contests/abc405/tasks/abc405_e)
  - 順序制約の境界となる要素を固定し、その左右の並べ方を `Comb` の積で数える。
  - 何を先に並べると残りが隙間への挿入になるかを考える。

- [ ] [ABC458 E - Count 123](https://atcoder.jp/contests/abc458/tasks/abc458_e)
  - `2` を先に並べ、前後にできる `X_2+1` 個の隙間へ `1` と `3` を分配する。
  - 同じ隙間に `1` と `3` は入れられないので、`1` を入れる隙間数を固定する。
  - 「使う隙間を選ぶ方法」と「同じ値を各隙間へ分配する方法」を、それぞれ `Comb` で数える。

- [ ] [ABC266 G - Yet Another RGB Sequence](https://atcoder.jp/contests/abc266/tasks/abc266_g)
  - 隣接する `RG` の個数を固定し、ペアを一つのブロックとして扱って残りを配置する。
  - 隣接条件をブロック化と組合せへ変換する発展問題。

### 走査・データ構造で寄与をまとめる

- [ ] [ABC378 E - Mod Sigma Problem](https://atcoder.jp/contests/abc378/tasks/abc378_e)
  - 区間の右端を固定し、累積和の差とmodで折り返す回数に分解する。
  - 得意な右端固定と、寄与のまとめ方をデータ構造へつなげる。

- [ ] [ABC356 E - Max/Min](https://atcoder.jp/contests/abc356/tasks/abc356_e)
  - 2要素の小さい方と商を固定し、大きい方の値の範囲ごとにペア数をまとめる。
  - 値の出現回数と累積和を使った、ペアの寄与の高速集計を練習する。

- [ ] [ABC306 F - Merge Sets](https://atcoder.jp/contests/abc306/tasks/abc306_f)
  - 集合のペアを直接処理せず、各要素の順位への寄与に分解する。
  - ソート順の走査とBITで、それまでの集合から受ける寄与をまとめる。

- [ ] [ABC276 F - Double Chance](https://atcoder.jp/contests/abc276/tasks/abc276_f)
  - 2回選んだ値の `max` を、各要素が最大値になる回数として数える。
  - 要素を1個追加したときの寄与を差分更新する。

- [ ] [ABC384 F - Double Sum 2](https://atcoder.jp/contests/abc384/tasks/abc384_f)
  - ペア和の値を2で割れる回数ごとに分類し、条件を満たすペアの寄与を集計する。

### 式展開・差分を使う発展

- [ ] [ABC399 F - Range Power Sum](https://atcoder.jp/contests/abc399/tasks/abc399_f)
  - 全区間の区間和の `K` 乗を、累積和と二項定理で分解する。
  - ABC471 Eの2乗展開を `K` 乗まで発展させ、右端を動かしながら必要な累積値を更新する。

- [ ] [ABC407 F - Sums of Sliding Window Maximum](https://atcoder.jp/contests/abc407/tasks/abc407_f)
  - 各要素が区間の最大値になる範囲を求め、区間長ごとの寄与を台形として捉える。
  - 全ての長さへ台形を高速に加えるため、2階差分で傾きの変化点だけを更新する。

- [ ] [ABC420 F - kirinuki](https://atcoder.jp/contests/abc420/tasks/abc420_f)
  - 各長方形を直接調べず、行を固定して長方形の寄与をまとめる。
  - 単調スタックなどの要素も強く、寄与だけの練習としてはかなり難しい。

- [ ] [ABC438 F - Sum of Mex](https://atcoder.jp/contests/abc438/tasks/abc438_f)
  - 木上の頂点ペアについて、パスに含まれない最小の頂点番号の総和を求める。
  - 条件を反転して数える寄与問題だが、木の構造の扱いも必要な発展問題。

### 考察チェック

1. 何を一つ固定するか。
2. 固定した要素や組が、一つの対象へいくつ寄与するか。
3. それを含む対象は何通りあるか。
4. `Comb` を使うなら、必ず選ぶ要素を除いた後の「残りの候補数」と「残りの選択数」はいくつか。
5. 小さい `N, K` における実際の登場回数と一致するか。
