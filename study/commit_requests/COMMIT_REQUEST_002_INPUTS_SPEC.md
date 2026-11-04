# COMMIT REQUEST 002 — INPUTS, EVIDENCE, SPEC AND ANALYSIS CODE (second commit)

**From:** BUILDER (no Git commands run; Amendment A4 host-Git mechanical protocol)
**Written:** 2026-11-01 UTC
**Boundary:** post-seal evidence/spec commit, per sealed DESIGN.md §14 item 2 —
committed before any result computation output. Parent must be the seal commit
`9d3ed18144d4cebc2b3c511ad596f3496e833be2`.

## Suggested commit message

    Study 0: pinned inputs, evidence, frozen rules, environment, analysis code

## Pre-commit verification for the coordinator

1. HEAD is the seal commit `9d3ed181…3be2`; `DESIGN.md` working file still hashes to
   `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06` and is NOT restaged.
2. Stage exactly the 378 paths below; every byte count and SHA256 must match.
3. The only remaining untracked path after staging must be
   `study/commit_requests/COMMIT_REQUEST_002_INPUTS_SPEC.md` (this file; queued for the next
   boundary). Any other leftover (including any `.DS_Store`) is unexpected: report, do not stage.

## After committing — host execution request (sealed DESIGN §13; study/ENVIRONMENT.md)

Run from the repository root, in order, and capture each command's full stdout+stderr to
`study/run_logs/RUN_00N_<name>.log` (files to be committed at the next boundary):

```
mkdir -p study/run_logs
env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/test_fixtures.py \
    > study/run_logs/RUN_001_fixtures.log 2>&1
env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/compute_study0.py \
    > study/run_logs/RUN_002_pipeline.log 2>&1
env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/compute_study0.py --out reports/repro_check \
    > study/run_logs/RUN_003_repro.log 2>&1
diff -r reports/tables reports/repro_check/tables >> study/run_logs/RUN_003_repro.log 2>&1
shasum -a 256 reports/results_study0.json reports/repro_check/results_study0.json \
    >> study/run_logs/RUN_003_repro.log 2>&1
env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/independent_check.py \
    > study/run_logs/RUN_004_independent.log 2>&1
```

Inputs: `data/raw/**`, `data/COVERAGE.json` (frozen by `data/MANIFEST.json`).
Expected outputs: `reports/results_study0.json`, `reports/tables/T01…T11*.md`,
`reports/repro_check/**`, `study/run_logs/RUN_001…004*.log`.
Report back: each command's exit status, the four log files, and
`shasum -a 256` of `reports/results_study0.json` and every file under `reports/tables/`.
Every command exits non-zero on any internal check failure; if any does, stop and report —
do not re-run with modifications. The builder inspects the committed logs/hashes next.

## Paths to stage and commit — exactly 378

| path | bytes | sha256 |
|---|---|---|
| `data/COVERAGE.json` | 3022 | `61311b002808ae175c18899e1f14076cd7b59a87b9a0544eaf466c1088ade230` |
| `data/MANIFEST.json` | 57816 | `bea49ac4a455b9742918adb62d7dd5dfe7538d05c31a56c3b9b30793b0ba459b` |
| `data/raw/coinbase/BTC-USD_pages.ndjson` | 41272 | `fe8f5fdbb39d027e0ea7a55036fd5528950adc20b94877d32de92a86c5c66005` |
| `data/raw/coinbase/ETH-USD_pages.ndjson` | 41272 | `be7f2d0ce3030a1bbb53b736ce23f8104cdc12b3ba7054ef47b3d86b77567f6c` |
| `data/raw/coinbase/BTC-USD/page_0000.json` | 18303 | `b61df93d6b96883e37fb50b5fbc26de793381bcea0ba80edfd72b54fabe83f0d` |
| `data/raw/coinbase/BTC-USD/page_0001.json` | 18299 | `80ad8c8515bfc855349d503933ce0d371e93b57517719d003f2841f1dd86d6ba` |
| `data/raw/coinbase/BTC-USD/page_0002.json` | 18280 | `d4d70e38d832615392508f8730166df08a816ed3c4dc4b426e3cf72806d34b64` |
| `data/raw/coinbase/BTC-USD/page_0003.json` | 18295 | `f992a81860ae75fcc87a3d38bfda2c2d796004c067dcb8e8000d875bdce35429` |
| `data/raw/coinbase/BTC-USD/page_0004.json` | 18342 | `b0377839934f94b4ae173fc01c30109dc323d326a9787344a6f737bc7e5060c1` |
| `data/raw/coinbase/BTC-USD/page_0005.json` | 18288 | `432ce430a18133a3724d86cfbbe8781f7bda09e84efdfdadcfdba2f171d2e2fd` |
| `data/raw/coinbase/BTC-USD/page_0006.json` | 18306 | `dcce1ce1b37c38ed3df58a1c3e294ac584bd1d094952fe23a1f458b2527f6d71` |
| `data/raw/coinbase/BTC-USD/page_0007.json` | 18311 | `ddf25acaf13f0c26f96f381ec1b4a5a6c64c94de013df8f32d62d4c63991f86d` |
| `data/raw/coinbase/BTC-USD/page_0008.json` | 18334 | `434cf492c1134bec4ea22607e7b26fde5ce5baa00fc6fd1334266957c98ec5d6` |
| `data/raw/coinbase/BTC-USD/page_0009.json` | 18381 | `628c801e3d3fdff1d54b1ef57c74248496732d34afae1467087b7ee9115be348` |
| `data/raw/coinbase/BTC-USD/page_0010.json` | 18285 | `dfaaaf858673aca632cf7d57f5e9ec46343e84a9a114c86f1b10219782cfa0ea` |
| `data/raw/coinbase/BTC-USD/page_0011.json` | 18311 | `19de45408516993cec469cd48d1ce295abb1d1bc902522ab1f849b50291ee82c` |
| `data/raw/coinbase/BTC-USD/page_0012.json` | 18297 | `facd8d5a151cda10f84d6782bceec5719909a92494b7accc63da84e45804b6f4` |
| `data/raw/coinbase/BTC-USD/page_0013.json` | 18294 | `cc44f5cb487d06b2006fcd28d4bfd6f5551c11a349bf437b9f41726af2f29d12` |
| `data/raw/coinbase/BTC-USD/page_0014.json` | 18287 | `5dde6dd5311f2cf85b62dc8a41be53772b10a67378f773e6584cc8dba09853ec` |
| `data/raw/coinbase/BTC-USD/page_0015.json` | 18279 | `8afd360298b407795bb2aff7d4c47371e3b899e74628d71d586229afa97a3e93` |
| `data/raw/coinbase/BTC-USD/page_0016.json` | 18344 | `4f2f7354c65b0ba77e43b96be9e9d86476bd9ba48ea5b3be8556d63eec385ba8` |
| `data/raw/coinbase/BTC-USD/page_0017.json` | 18295 | `34f463f5ed941dba928ad4596d76fcc2599e776b2c71375e8a346ba0fcb5da95` |
| `data/raw/coinbase/BTC-USD/page_0018.json` | 18230 | `5f2559f3932fb266979cc3b88ba77beef3c50e1f7df94bbd5eb6a00996a05941` |
| `data/raw/coinbase/BTC-USD/page_0019.json` | 18262 | `e42414ce9582e36371fc8c361f6bce1bbcf9bac839b315beddb1ec3d649d7191` |
| `data/raw/coinbase/BTC-USD/page_0020.json` | 18282 | `36bf5a62aa671aa302bfbb77734e449553ab9183f2368fd4095a3f3bfb37529c` |
| `data/raw/coinbase/BTC-USD/page_0021.json` | 18375 | `3c020197979a2e12bc76baaa4dbfdbb887d0743a68e35c864fdd260406aaf5e3` |
| `data/raw/coinbase/BTC-USD/page_0022.json` | 18252 | `6ac175b836fcf9e0ef4b6096312ac706c9c93290c1bbdb1d970e6a6f48b63e1e` |
| `data/raw/coinbase/BTC-USD/page_0023.json` | 18221 | `c91717204e0f2dca6e138c09f9c203996678f8442542f1665f29ed9245c92ef4` |
| `data/raw/coinbase/BTC-USD/page_0024.json` | 18259 | `1136b4970f7e7ed5613aa06c80f271eb26b3d4f55e46ed3fcaced3dea4689d63` |
| `data/raw/coinbase/BTC-USD/page_0025.json` | 18288 | `ff0ea8f71f744f93370f28bb17baa12402cfdf34c6e353c899a7f382251ef751` |
| `data/raw/coinbase/BTC-USD/page_0026.json` | 18301 | `84e00d60f7bf0e5e7593201f3da6ad51c1f38ee5c6957a7f076338640dfce880` |
| `data/raw/coinbase/BTC-USD/page_0027.json` | 18214 | `3f6c8a89663c296dcf067d8f99990ff88e810e51a3b046681fe0523416c6bcd7` |
| `data/raw/coinbase/BTC-USD/page_0028.json` | 18160 | `04435fc6a5860cf96a1919173be87303b46356686162840782a79b014e7f784d` |
| `data/raw/coinbase/BTC-USD/page_0029.json` | 18256 | `814bf89fb09df129e82afb390abd0518a784918644ab95a69d07adcf6d5afd83` |
| `data/raw/coinbase/BTC-USD/page_0030.json` | 18286 | `2e88e2eaa7b34a41cf585f8c1074f47c9046500e29b4cf5745f6a11f78a7680f` |
| `data/raw/coinbase/BTC-USD/page_0031.json` | 18244 | `945150beb591de2ae7ec1c8d742052781e14df8b8ec2d34499f1951d5b1a21de` |
| `data/raw/coinbase/BTC-USD/page_0032.json` | 18230 | `b976b896f09c0bb39dcbf6f24e8e0c80a03d8366b1e8d4859905fe22a5e235de` |
| `data/raw/coinbase/BTC-USD/page_0033.json` | 18306 | `7535f75fab45e4628a06c7f1489f702effc2d81e26b85e9c663945e0342eb1df` |
| `data/raw/coinbase/BTC-USD/page_0034.json` | 18257 | `a01120f8afc38fb055de68c97cbcc8bf68d37764c961bb90f0ffe4394966e076` |
| `data/raw/coinbase/BTC-USD/page_0035.json` | 18208 | `b059a6301176e2b1b148b2f29c8a44a5c34162ce8cddb199e1db389eb2e25c5f` |
| `data/raw/coinbase/BTC-USD/page_0036.json` | 18189 | `b85504b4a89db76d473de8e10a05e5f0aed51bd6cbbff27d25dd94b70e6ab1f2` |
| `data/raw/coinbase/BTC-USD/page_0037.json` | 18190 | `377376e43a1a836be387b134b5d8ec339b775af435aebd87858f6ff1a97b2cf2` |
| `data/raw/coinbase/BTC-USD/page_0038.json` | 18252 | `a0bc201ad836f832cee98ba0351b9facebe5974cefbe819cc960c2b3faf906a5` |
| `data/raw/coinbase/BTC-USD/page_0039.json` | 18200 | `fa34199f128938840f8d41839d965770a39f149e8394cd60a0f8e3b5ac96ab08` |
| `data/raw/coinbase/BTC-USD/page_0040.json` | 18254 | `69bcc7d406671843909e4cbfb5841d3212d2c80a30658a59f9c36d50708e57f8` |
| `data/raw/coinbase/BTC-USD/page_0041.json` | 18285 | `9ab87850509bc3445d7a36ac5d5e62aefb75cc77e63ef86bce5e6a4220451acc` |
| `data/raw/coinbase/BTC-USD/page_0042.json` | 18398 | `285450b2cd858329fa1aa25350cab6685c6b95fb57e14553ab37b61d347b214e` |
| `data/raw/coinbase/BTC-USD/page_0043.json` | 19035 | `05eeaa11e5b275d01a6865d137b958b48135980da5582425a8a3c004c941099b` |
| `data/raw/coinbase/BTC-USD/page_0044.json` | 18224 | `e7a22df7b0c1b9450d362c6ee1aee15322a80201850038986dda535991bc1422` |
| `data/raw/coinbase/BTC-USD/page_0045.json` | 18351 | `56f064c591d678c1004a72b77e030b4b8f91ee5e7e92aba4a9819fd484bbb02b` |
| `data/raw/coinbase/BTC-USD/page_0046.json` | 19383 | `dad04e6eb6a422d08beca748b9ee4dae2806cf873b0fe7d1d6366ec875803ca0` |
| `data/raw/coinbase/BTC-USD/page_0047.json` | 18492 | `ba39c8dc9f6e78750ffec97c104eb8c7269ee688c8f4082e2963040b9978b36e` |
| `data/raw/coinbase/BTC-USD/page_0048.json` | 18169 | `de5e30f8b3b0fc77d5b35769246ceba14c960565ea3e996a5f865c14d744bb26` |
| `data/raw/coinbase/BTC-USD/page_0049.json` | 18236 | `3977803cfda205c0a78428f6c8c3c721f1334089f0cd67564b673b925c5ba717` |
| `data/raw/coinbase/BTC-USD/page_0050.json` | 18242 | `072f58f29dfed9b9b799d177884105f3d5e24e37b421d4b35887c8e35767789a` |
| `data/raw/coinbase/BTC-USD/page_0051.json` | 18213 | `f2d8acc4ea75718780293bd136df1093deb24ed56086b2f03a56d5f48ddf893a` |
| `data/raw/coinbase/BTC-USD/page_0052.json` | 18244 | `af841b16a33947f20b736b03373401a5d4159be4f73621e1c2f593c589398600` |
| `data/raw/coinbase/BTC-USD/page_0053.json` | 18179 | `6981e7ef594956d903088fae5661de3785b81216c6d02db6355586cec4b46e05` |
| `data/raw/coinbase/BTC-USD/page_0054.json` | 18262 | `fa68e4a9e4ea25ead80ae3e96e0b4ee194100f29a81276667bccf2432e05c87e` |
| `data/raw/coinbase/BTC-USD/page_0055.json` | 19360 | `ecef6297e09442fdce7a69bf43f2254959638d3758e91b4a6b6116b58334f824` |
| `data/raw/coinbase/BTC-USD/page_0056.json` | 19375 | `f5da101a26a081ed8a9edb7b359fe63df54b9f25a9709e54cbbc2f830ef854cd` |
| `data/raw/coinbase/BTC-USD/page_0057.json` | 19337 | `75cc23283af5268a11f4149bc18a1f9518d185f9200a5e6e7358693c78b17ea9` |
| `data/raw/coinbase/BTC-USD/page_0058.json` | 19281 | `152fb56a4616e1875c6ba8c92921c7a8f50f9961fc23cf08c25a946bbe932f62` |
| `data/raw/coinbase/BTC-USD/page_0059.json` | 19300 | `d7373cb1f2b553f52736a652a7905856e717779aecadd8edc25520b9d0059ad7` |
| `data/raw/coinbase/BTC-USD/page_0060.json` | 19341 | `750a2a5c593dc065125cd9d9e6e79bd41157a8736c2edff44ac7169f0aa165ad` |
| `data/raw/coinbase/BTC-USD/page_0061.json` | 19298 | `780f493efa2e5ac56ed8165c2f83d339b1f53ac19410b9b6fc6d38929bb68526` |
| `data/raw/coinbase/BTC-USD/page_0062.json` | 19298 | `72563127431ebc5ef40dcc2ca1ca5b991d92915aee1c36504d58d66b761f3e00` |
| `data/raw/coinbase/BTC-USD/page_0063.json` | 19377 | `bc51fc4c125065baa7c19d0dd97083a1564fbdb2c790edf6c334d7be984fa6c9` |
| `data/raw/coinbase/BTC-USD/page_0064.json` | 19348 | `0505e2b791b40dc972b4d9871d125e933f6df8e4b3556fb6e85f1f531835941b` |
| `data/raw/coinbase/BTC-USD/page_0065.json` | 19219 | `afebc57e7b0b2d8be20355f8d95c3d3498a22f4cc7ff2d7848e049acd92938e1` |
| `data/raw/coinbase/BTC-USD/page_0066.json` | 19253 | `bb7da556ad3fc8e988db4f619ccea94242fb667978705c83ee2b8b875dd94f80` |
| `data/raw/coinbase/BTC-USD/page_0067.json` | 19259 | `101d77743fbfb463a176b16cb7bf62aa7610d7081032aa051c016492dd3daf6f` |
| `data/raw/coinbase/BTC-USD/page_0068.json` | 18858 | `329f4e01c95d58570eaa60837e597ae28419146811eb2a5a7562865d581b749f` |
| `data/raw/coinbase/BTC-USD/page_0069.json` | 19240 | `72a4284f6fdfef621c2fcfc29b42890d87cb9b5fae264d837adb6b481a9969ab` |
| `data/raw/coinbase/BTC-USD/page_0070.json` | 18019 | `5e3532d76f224b91fddcf2ca53d5f9073f41ee255012e096f75ef08551cc1198` |
| `data/raw/coinbase/BTC-USD/page_0071.json` | 18063 | `37eb594ec7e1651d1c256a53c13b4adffb3fb2740b6c436df3329d0878ec243f` |
| `data/raw/coinbase/BTC-USD/page_0072.json` | 17819 | `cc522e70ce1924adc7b7c4f0db05e0dcb166b294efdf0fa338e7ffec9fee486e` |
| `data/raw/coinbase/BTC-USD/page_0073.json` | 18006 | `d4f9d395a0afe172cbe63d0c571851967e696fd9f8d173a0f362bb95f8163437` |
| `data/raw/coinbase/BTC-USD/page_0074.json` | 17970 | `e0bd984613b8011e5f90a21e962b20766af8ce7efa79940f83ce8bb923d5c94a` |
| `data/raw/coinbase/BTC-USD/page_0075.json` | 17916 | `73d15641e4c0a0616650ea45f57b063998d922b7f846cdf7958f9340703adc3f` |
| `data/raw/coinbase/BTC-USD/page_0076.json` | 18082 | `05955990505a023d6e12097f5d20f9fa958fa168bc4da1c6b40ea3de543b6cd7` |
| `data/raw/coinbase/BTC-USD/page_0077.json` | 18042 | `862165dcfa59424311002dd3bd80b04c28ad93db4e51f673f46253fa0808eb03` |
| `data/raw/coinbase/BTC-USD/page_0078.json` | 18114 | `bc9223d575a6b544ab7304219343b3f23c42b7206c41e1c78d78139e7d0df626` |
| `data/raw/coinbase/BTC-USD/page_0079.json` | 18224 | `86e87d03386b99852b20d2ec0a9b0bc00d6007e5272b24e05c644700c9249a5d` |
| `data/raw/coinbase/BTC-USD/page_0080.json` | 18043 | `fc218b1815537cae61ab9752f70987ce84d3076e52e3a332e4d5ced3fc7e031c` |
| `data/raw/coinbase/BTC-USD/page_0081.json` | 18030 | `2bc0d767c8d9835769524de466f50c303a481e3463fa568245203ee538121a5e` |
| `data/raw/coinbase/BTC-USD/page_0082.json` | 18175 | `00d018a67fcc852f8c831f042a3287c711ab3cbd391cc3fdc07b5b4725c1244b` |
| `data/raw/coinbase/BTC-USD/page_0083.json` | 18072 | `c90ae0665cbe10dfb2fe037966ba3fef8d8fb47ac98d832c39f3c8fba8a78d6a` |
| `data/raw/coinbase/BTC-USD/page_0084.json` | 17705 | `4bd53099040f2236b2e7b1f79320247b8b51a8447df85d7c8b8fc01baadc842b` |
| `data/raw/coinbase/BTC-USD/page_0085.json` | 18086 | `120aa1001207236bfa07e029e2edff100165731dceeee837690a4bb6067573fe` |
| `data/raw/coinbase/BTC-USD/page_0086.json` | 18128 | `387d087103965d2d7f0c52894f8d91b363c744b8e42dbd0a223011fb090d20d7` |
| `data/raw/coinbase/BTC-USD/page_0087.json` | 18173 | `04e045a3a93b1ab84ca6a8f03a7b66ff4987add6f86c2f715f440cded4f883c5` |
| `data/raw/coinbase/BTC-USD/page_0088.json` | 18157 | `8b321aadefc73d6e7d966e46623c98b2cc43b891068348b0bff82b731c62faf6` |
| `data/raw/coinbase/BTC-USD/page_0089.json` | 18040 | `1f870c8761f01a31a827919225c74d943bdbd5541f10eac444600863e7e41152` |
| `data/raw/coinbase/BTC-USD/page_0090.json` | 18144 | `714f4eee85d7da02f96b9cbc8512f43fa1308b651bfea5dff4fcdb7f6a7880dc` |
| `data/raw/coinbase/BTC-USD/page_0091.json` | 18145 | `0c2ccf2c5f17e48cf8999c8a371847d4aecb78c0a606d11174aab63da90bd85e` |
| `data/raw/coinbase/BTC-USD/page_0092.json` | 18183 | `0a52e7df63ea07b110eaeec56d8fed627f0f08b6d72b6bf1b89e3654234a87d5` |
| `data/raw/coinbase/BTC-USD/page_0093.json` | 18053 | `83a784f9cdff26ac8f73a3439ca8c18ba58a0cb97a9627ee070b8fe065e735e6` |
| `data/raw/coinbase/BTC-USD/page_0094.json` | 18090 | `5540548cdb51e80fc2a473fcd6cc527816cab7181fe1819a7893a2ad9d9f011b` |
| `data/raw/coinbase/BTC-USD/page_0095.json` | 18096 | `1dfb0c0651469d2bec1316f4f788550a1eab43fc67475b0f3a66d591400181b7` |
| `data/raw/coinbase/BTC-USD/page_0096.json` | 18191 | `588ade5a30cdd4d815574696b27948f0982413e53bbb5d91deb6506105188a54` |
| `data/raw/coinbase/BTC-USD/page_0097.json` | 18130 | `47c168c6bcc524af86ae95461ce5253a029c2a3defc0e56d7830a7628a29b054` |
| `data/raw/coinbase/BTC-USD/page_0098.json` | 2908 | `c1cdb7551edf5dfde935040e243ad2b491f504089f46149e6a660a66014e5a31` |
| `data/raw/coinbase/ETH-USD/page_0000.json` | 17421 | `96e4dc697afddab14a2477463dc57c64d26435119e798dea3f7f504e8d1b1765` |
| `data/raw/coinbase/ETH-USD/page_0001.json` | 17467 | `131c3d7fa34bf5f3041f4e897b3966cdd09e4ec2e3a12e218ee575853b57cd36` |
| `data/raw/coinbase/ETH-USD/page_0002.json` | 17434 | `087f8f0535ca34b0f6f05ed3e693678c61d9cc2c83a33d7b36c0102fc3285b97` |
| `data/raw/coinbase/ETH-USD/page_0003.json` | 17387 | `6309068f0e2f48d17c8861f6a4e207108ce9197bb9ebf1a9f6caba6478e7a0c2` |
| `data/raw/coinbase/ETH-USD/page_0004.json` | 17448 | `1f87f5c0c0c20a927561b72864e61bc2301baa02231cb0c285efb4795b6e4a55` |
| `data/raw/coinbase/ETH-USD/page_0005.json` | 17436 | `8daac5313e932a49382f2ec3319a4981c0a1ac0dc865aad26e37bbc7384a89ee` |
| `data/raw/coinbase/ETH-USD/page_0006.json` | 17439 | `80e3129a59aaae2d3363468cbe010095fde9e8ebb24a68b2c78caa3d0b1bf424` |
| `data/raw/coinbase/ETH-USD/page_0007.json` | 17439 | `c061ab948a1f4a0aa43c268bc6e50397c5ef85092c7f5870704ef1a63cee7742` |
| `data/raw/coinbase/ETH-USD/page_0008.json` | 17442 | `c24abf074a2e56b79249b8479e48d1695ab04653deb980bc98b51f3b6c3e9e0e` |
| `data/raw/coinbase/ETH-USD/page_0009.json` | 17440 | `1b140d63d6417d4f4745f7238085c8bd78f10dd35625a30951c2d1617d54601e` |
| `data/raw/coinbase/ETH-USD/page_0010.json` | 17454 | `fe9502f966249ab45234239486c5f9174629c0a6a9683d9480d0acf65fed3c9d` |
| `data/raw/coinbase/ETH-USD/page_0011.json` | 17458 | `3f9f1996736281564a98b15632a1d973040c5b85e6a7b83809e2bc0ea637c893` |
| `data/raw/coinbase/ETH-USD/page_0012.json` | 17431 | `c18ef996b91e1082ca46e5334f0564c44601e87774e9c1ba5736ec76260f4e14` |
| `data/raw/coinbase/ETH-USD/page_0013.json` | 17486 | `d3b20e82d736af7e1aa8b17ced310d77369a148fda4d04a980092791961dd600` |
| `data/raw/coinbase/ETH-USD/page_0014.json` | 17483 | `ef58f630e6232ff10d4e07885d34b025b3775664a4474a8492eb3b5b15555601` |
| `data/raw/coinbase/ETH-USD/page_0015.json` | 17494 | `a3264441afbaf7fcd2ac32300c1e2e1cc853d99f3a30586b8020a38f54ed9e1b` |
| `data/raw/coinbase/ETH-USD/page_0016.json` | 17522 | `652a0a1ec89d6675f973a874a43977a0e3884596bba7cc22470828b19d00918b` |
| `data/raw/coinbase/ETH-USD/page_0017.json` | 17446 | `ed78f4c7a513f72b473fa60a45acdd3eb0b21c15cf51391f4f13a0c891694f8a` |
| `data/raw/coinbase/ETH-USD/page_0018.json` | 17418 | `99200aade2f8b38d10df47b75796c14e3f14319b6c4252a5f1b0bd5c0f428f26` |
| `data/raw/coinbase/ETH-USD/page_0019.json` | 17465 | `2e7259a8b394f71ebfa2e97dc843509c49b8b2d86bf9fa5b57553d6523c5b6c7` |
| `data/raw/coinbase/ETH-USD/page_0020.json` | 17464 | `145cb8525465c8f8afdcee84cf905609382d0ce2f8e5e122f0196a0554f5244a` |
| `data/raw/coinbase/ETH-USD/page_0021.json` | 17497 | `b2c26299b03522c8aea71c4f806386839c99f778dc8bdccbf22e9aed1a16b6f4` |
| `data/raw/coinbase/ETH-USD/page_0022.json` | 17475 | `f82cd167f95b229a6b006abc3bc9dbab72be053bd69953789e3d0bc13ee65f19` |
| `data/raw/coinbase/ETH-USD/page_0023.json` | 17463 | `b1821ff5fed3419d83c2a3dff68b67e00a0c58b4de97ffaedc09a0b924e965cf` |
| `data/raw/coinbase/ETH-USD/page_0024.json` | 17440 | `c110ab1a3035b7482ada478336d10ea9d112c85d5e90ff75ab3ff56e5e0d8629` |
| `data/raw/coinbase/ETH-USD/page_0025.json` | 17471 | `56b17a716ad204d5fc2abbe4c721c9ebdac70c15a1c071b7a4c19cc5334e4bcf` |
| `data/raw/coinbase/ETH-USD/page_0026.json` | 17482 | `842e2fca41a7d83afad3e774305993b86fc8ff30f1b293bc7d77fb7fd66c8bca` |
| `data/raw/coinbase/ETH-USD/page_0027.json` | 17421 | `6ee4431cdc297c7fcc188c4a8beeef6717e804c065e01cf067934bab24cd1a4c` |
| `data/raw/coinbase/ETH-USD/page_0028.json` | 17387 | `edd6a150b8095ee9dc0ea3def5fbedf588508fd17ad5a7d1bc6df5faaf8bbc2c` |
| `data/raw/coinbase/ETH-USD/page_0029.json` | 17442 | `9e26536d7a8d3c54a7d407b53efcf1c32c615508ffed6536fcf328999ff22e21` |
| `data/raw/coinbase/ETH-USD/page_0030.json` | 17426 | `338559768d3bb49c6b0d488b572938ff2eacbc216cf6f85c0406241677d55dbc` |
| `data/raw/coinbase/ETH-USD/page_0031.json` | 17432 | `1ecaaa18bf006afdbc7d1c1d0cae9e06734bc10bfe7f04d6f51c367238631554` |
| `data/raw/coinbase/ETH-USD/page_0032.json` | 17526 | `504152cce5ada6529bf66bacaae8076377918aeaa0ab7d48ec49c9e5ac49c178` |
| `data/raw/coinbase/ETH-USD/page_0033.json` | 17431 | `0eb39fae4b8c8a4b55b6c809f50945d5f590980adb233252bb2a3d36934ec7df` |
| `data/raw/coinbase/ETH-USD/page_0034.json` | 17412 | `8dd819a3861d887ba81d262ba2d4232dc78eecca2776efa336ded3a861155172` |
| `data/raw/coinbase/ETH-USD/page_0035.json` | 17439 | `92f6cca230b5ac22b8d719fa476f3168d5ce5569f70601ca5ab7d9b47a3f2d70` |
| `data/raw/coinbase/ETH-USD/page_0036.json` | 17432 | `2fa97baee76cb2a7cb8338f80520f6f70f442d3e59271bc0098843676f0e930f` |
| `data/raw/coinbase/ETH-USD/page_0037.json` | 17387 | `e6a8e342fff0c43d3c422f0736d4f96b87fe3038ce015f1fc3ddf8526ef5a2a6` |
| `data/raw/coinbase/ETH-USD/page_0038.json` | 17449 | `b7c0ac67c107bff527d4d7fd81888eed2b08daa7b19f05f1b62b3e2df0acc218` |
| `data/raw/coinbase/ETH-USD/page_0039.json` | 17441 | `921d13630e5535f7a54bdd10014848332c8fc513a1911f2de5f15bc97d94b6e3` |
| `data/raw/coinbase/ETH-USD/page_0040.json` | 17524 | `7c1cac5475fb09c2012d47a5959f708c83ee3b3c2309605f2c242d0cbdb57043` |
| `data/raw/coinbase/ETH-USD/page_0041.json` | 17447 | `39e51dc54a62b837b320deb4d162fb2f71ca83f9ae2a60217c1ab491a089e953` |
| `data/raw/coinbase/ETH-USD/page_0042.json` | 17446 | `fd2663c391961eb683eb8a896976723c856ac2fd6b9b1a5478717348c1b15100` |
| `data/raw/coinbase/ETH-USD/page_0043.json` | 17469 | `049dc7253518cd1fc76f514b4dd7b9b892c6cf96437b42a45a2ca68fddcf281b` |
| `data/raw/coinbase/ETH-USD/page_0044.json` | 17368 | `768fe33876aca6beff4f0200f4e2401ea01c60602af7ba704ba359062cac6bb1` |
| `data/raw/coinbase/ETH-USD/page_0045.json` | 17469 | `27d8083908c8732f860fd85c43f1c4c4f390d62b7b6d7a9a48fd1bc6c2a0733a` |
| `data/raw/coinbase/ETH-USD/page_0046.json` | 17487 | `eeea5013200840b3600324b847a85c3d0214e719cc103092e900cae4987d4a22` |
| `data/raw/coinbase/ETH-USD/page_0047.json` | 17568 | `83000f1a06325f7d3aeb6eac5a7045546376fe19ae80391cceb995d5a9721610` |
| `data/raw/coinbase/ETH-USD/page_0048.json` | 17490 | `93a0a456dfde2d561c16efd37b37bc09b4e76c79f0bb75b7505582f81e395160` |
| `data/raw/coinbase/ETH-USD/page_0049.json` | 17558 | `38bb1069ebecd7c87c083f6f2072847e32b6b848d1d7ffced38b0cd27834d369` |
| `data/raw/coinbase/ETH-USD/page_0050.json` | 17472 | `52ae4bfb9de93d4f36a5bc409a379c242ce640e9925f3cbd8c8e98ccdd243e87` |
| `data/raw/coinbase/ETH-USD/page_0051.json` | 17431 | `afd412dfce7ec9b809db278b23c1410bd146f103b0800ce9ad8938d85726a7ff` |
| `data/raw/coinbase/ETH-USD/page_0052.json` | 17527 | `1f4a327273a678dfac38698ce4cfac25a4b10b577bfa16119ab90974b4b120f0` |
| `data/raw/coinbase/ETH-USD/page_0053.json` | 17488 | `207f11fdd11268b9fa707ee4679547f654e217d01acb658065fc1aca07c97fcb` |
| `data/raw/coinbase/ETH-USD/page_0054.json` | 17489 | `8157098e8cfbb3c0103d1ce9ee795a6f5e4af23cbc63fba02dc0e309ceae92e0` |
| `data/raw/coinbase/ETH-USD/page_0055.json` | 17499 | `741cdc339891ebbc6595635cfb358af15dff7c9c6e0e6b711593eb24991e8ef0` |
| `data/raw/coinbase/ETH-USD/page_0056.json` | 17449 | `f9b70ffd52fb8f8bf41e26ab08ed5dd37dcff65d254163cb0bb9f620319fcd0b` |
| `data/raw/coinbase/ETH-USD/page_0057.json` | 17470 | `75eaecedae0c725cc008de743a65efd84c15176d619eb9d739ca0d1ed9af8100` |
| `data/raw/coinbase/ETH-USD/page_0058.json` | 17432 | `5af97ad78d45fcce02cc6ee1d1e87442c6658208f957186be3729008fcc00bc6` |
| `data/raw/coinbase/ETH-USD/page_0059.json` | 17433 | `511ba1ff3cbd92f66540d5913a0d9aa62e72d50954c0ca3ae6ec6ef6ebb9843b` |
| `data/raw/coinbase/ETH-USD/page_0060.json` | 17438 | `94f05815a8bae5a7c371fd45c6535973f276518a278410f2a59bc4be2758db77` |
| `data/raw/coinbase/ETH-USD/page_0061.json` | 17449 | `f3da07cd9b980630e3e286cd54487c4f4fad0dd99f8593d7962683cdbc367fc1` |
| `data/raw/coinbase/ETH-USD/page_0062.json` | 17493 | `066aead4c2158736f1e1d7dd2d727ae9a0438c88beba5d592bcb1f6c698e864c` |
| `data/raw/coinbase/ETH-USD/page_0063.json` | 17424 | `1e9b0558d5830f685b753d59fdbf5ea91ac8fd8b04ae0bbaff4c047926cd0553` |
| `data/raw/coinbase/ETH-USD/page_0064.json` | 17427 | `cd2e5c632e0bb9f022daa51548280a4e40f157e06e4db4653c3d52b2f5d5d09d` |
| `data/raw/coinbase/ETH-USD/page_0065.json` | 17329 | `5797715e3cfce42fc65191d61e4155d103fdfa883f94f61b168af04afd8378e9` |
| `data/raw/coinbase/ETH-USD/page_0066.json` | 17358 | `fad52e91ca8b71a1b802708e552dcbaec03c1c35e14a269e34c3cf3daf78edb2` |
| `data/raw/coinbase/ETH-USD/page_0067.json` | 17381 | `14a6f0f871fa8d71f1862967bb80b431454f12e947345d59e489a2c2dfc5d39f` |
| `data/raw/coinbase/ETH-USD/page_0068.json` | 17068 | `636f3b2ee420637f8bfa5808000a32229d3db6508d18c76075d05d732c9347b6` |
| `data/raw/coinbase/ETH-USD/page_0069.json` | 17394 | `f49ca1f100092a3135c33a2e3f4081beb0df0a082bcd8682b09bb8888679b7f9` |
| `data/raw/coinbase/ETH-USD/page_0070.json` | 17449 | `e30b3fb50cb0e2d65d2d6031fc3d09adf9117dac31e97958528d7b9d1a566995` |
| `data/raw/coinbase/ETH-USD/page_0071.json` | 17362 | `4dd5c201d0115c7c38cf41880ea67ca029d84cfaf9f657424fba45d311edca3f` |
| `data/raw/coinbase/ETH-USD/page_0072.json` | 17301 | `2e6996feafea126a986c77fc65aceaa8bb7ae4238d4f9bd043e34122f6244954` |
| `data/raw/coinbase/ETH-USD/page_0073.json` | 17313 | `17086b72420f5d00375cb86316a3e71cc4f48235ac0c0462a239809f88ebbf5c` |
| `data/raw/coinbase/ETH-USD/page_0074.json` | 17357 | `693704a27aba457e2e06bae83103c79db5490c33e7361bada35960ca546e41cc` |
| `data/raw/coinbase/ETH-USD/page_0075.json` | 17340 | `915777d1d7894b30fb81e992c5278e7664b3181cfd7feae9bbf4afdbe9cb8f9a` |
| `data/raw/coinbase/ETH-USD/page_0076.json` | 17518 | `1652063be0feaed28af50fdc283135d0c34853069ee2f6ea68ef959c3076e466` |
| `data/raw/coinbase/ETH-USD/page_0077.json` | 17406 | `b44911f28f4ee2609eba4f356583627d151c21936a8e92bdcb0e3a339ddaffe4` |
| `data/raw/coinbase/ETH-USD/page_0078.json` | 17434 | `80c6ab5abcb8fd61f90895248eb012b6466da538befc1028ca148863431dcae1` |
| `data/raw/coinbase/ETH-USD/page_0079.json` | 17408 | `899c3cc985b1b9cfef44a57bc940ec8071c3797028d9a4e0f12d550cc376a744` |
| `data/raw/coinbase/ETH-USD/page_0080.json` | 17449 | `9ab4e27d9e409e79fd337fd9127b249aa4d74d5baf602e98aceb4ae7c367ae33` |
| `data/raw/coinbase/ETH-USD/page_0081.json` | 17389 | `3d6070c489bb72ff626e8eff2c34790faaac4838e094588585c64dbfd3ed062f` |
| `data/raw/coinbase/ETH-USD/page_0082.json` | 17334 | `69f5873cc597eb30380d54c677d61069c713fbb88cd844dcf44a9a9ac511cb99` |
| `data/raw/coinbase/ETH-USD/page_0083.json` | 17325 | `83bb1be079fb951673a1492ecbb74c78ed75c0de60b0f8a383e25adf33550bff` |
| `data/raw/coinbase/ETH-USD/page_0084.json` | 17087 | `a60c066dace065c5f25455c484c914f0a546ab8fca183c9ae910691730e82e80` |
| `data/raw/coinbase/ETH-USD/page_0085.json` | 17395 | `a33887764472b5a04d56f7992b43e5b5f5a39af277dbbd4f1447ca0f8976fdca` |
| `data/raw/coinbase/ETH-USD/page_0086.json` | 17423 | `39bda3f9a7d393be4b73bf30bcc44c9af11970142650d23abdc2a219e1d7430a` |
| `data/raw/coinbase/ETH-USD/page_0087.json` | 17376 | `1650d9304228c161025936e3f017f1ec4f5ceec0f6a442fd3426a0622bf1c355` |
| `data/raw/coinbase/ETH-USD/page_0088.json` | 17377 | `271840f6b605fe0aad2bc907c8397142ae4d42ab11aae1984443781b9f726229` |
| `data/raw/coinbase/ETH-USD/page_0089.json` | 17383 | `02e5825c968395c73dbe7e68778555e5f15a0f5d850680d08ca284b06815b08c` |
| `data/raw/coinbase/ETH-USD/page_0090.json` | 17297 | `0edc1271349eeb2f1ffcee77900d82ac9b57331ca77e781aaae4b1c002eb4511` |
| `data/raw/coinbase/ETH-USD/page_0091.json` | 17318 | `371768161f0bb45093a07a6fd0993352e8babb825afc325af061aa37588fa42e` |
| `data/raw/coinbase/ETH-USD/page_0092.json` | 17392 | `92d5757853cce12f269d262918d8380767e2433fb4966f378e4d916c2d9a301c` |
| `data/raw/coinbase/ETH-USD/page_0093.json` | 17385 | `34abb883ee77b8dc25d50f92dc1ab50aed75140ec4056529b477d00dd8272160` |
| `data/raw/coinbase/ETH-USD/page_0094.json` | 17397 | `f0a1045b3952a4bb32fd81eac070c383610933ca2c3ae7b7ac2bee3db69d95ae` |
| `data/raw/coinbase/ETH-USD/page_0095.json` | 17389 | `0d6c678b31d9df33a41ae7a2ba0ef53e7b65d8a44d7b1a941347a6410b5fbddc` |
| `data/raw/coinbase/ETH-USD/page_0096.json` | 17420 | `f415d42e83c1a2a158f239dd72d8d49be53baafe7467db9b8872d2ee704aef1b` |
| `data/raw/coinbase/ETH-USD/page_0097.json` | 17465 | `01028dc330cd23807c69539c1230f7a9393081ec21fc1d9f6ff5c905d7d4a101` |
| `data/raw/coinbase/ETH-USD/page_0098.json` | 2788 | `18155de5b101eb264eca101ac844cc7aee0c9243553f709f44275cf381528007` |
| `data/raw/defillama/RETRIEVAL_LOG.tsv` | 483 | `4c8b7f78350252d15bc4a2689a6ad3d0ebc8a127d14fc59fa0a3f7652b073708` |
| `data/raw/defillama/chart_native_usdc.json` | 193137 | `5c562e7ef63a30d595daac67f2942371b98d07a2866dd4ecd70aecc9ddd530c0` |
| `data/raw/defillama/chart_usdc_e.json` | 235174 | `5aa1bbf38308373a00e5e6f6d292f7fb8ca0f0987c7c8afa28a848e7241a916a` |
| `data/raw/defillama/pools_snapshot.json` | 10964748 | `48fee47ebe9470c2c09a8b76879caecf590f0e96a8987e49e0de06bbc9c08cc0` |
| `data/raw/defillama_adapter_evidence/RETRIEVAL_LOG.tsv` | 4628 | `a7caf70b4d2e15ff5cd86bc74b12329f47ac95d5972f8492f71e433c05e949ca` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_03b47a004293.js` | 10423 | `6e64a56dc0d616ea2feff2261fbfa6b1ecf2d66da06d5ee009d150f11249a373` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_04bab22e688a.js` | 7551 | `d4e623b6452962ea08769b987b6f595d0660cea51c009ed1c5a63fde73bba0d6` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_22cd411350b3.js` | 13808 | `4e019c08e3a908dcf458958a9c1d9dd3e0daa86eb3c0c79d2edab1565b3dd5ff` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_3173abeb170b.js` | 10899 | `781fa1293a4d6c5f4e16db6a4991fd496f4b3c9f9973bd916f42c48dbec55ef5` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_395d7a1a6f21.js` | 6805 | `50d3b22d82f7b84bc0610a882c3d253acd54088963b2370b7c221c65ec4b9074` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_3b22a52d483b.js` | 7480 | `7ac0a7db4fa8ef9413a413ba937dbb7dd9d1e88ca1f857565c2485b9f88bb136` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_42ec40d6ddc6.js` | 6743 | `0ae5b5079443596821742fa7be58c8f7cfe16bea02e3f454cfb592ce1d3c14a3` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_4d3ff6cb4dd7.js` | 13767 | `6498cdfe1bd7d237ebd909d4bfe1c7d7590bc0163fb0145ceec305b03d1e9eea` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_6387427c97c5.js` | 18105 | `ab35fe5c071d0f691ef4b19320b1b942675cc5b539c32e5cf84a8ce5ba49e5ba` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_7f1523db861f.js` | 11872 | `2f6ccd59d4e53b9b507caad8e2f172833fc67755c788f33deab117e84dde5d70` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_a88b70c12f99.js` | 7793 | `9f5c28003bc0ab156c042a81830f4ada94d8a7ea33a0a2bf062de319bca55521` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_ae16804e6345.js` | 17304 | `27840c5dc0704af52e64b6c4946f6fcbb28971ca75ec2545fd24c2887d53ab1b` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_ce9bc01e61f9.js` | 11001 | `bdc21befd72b500d1e560ac1201252f52739de59b0fa4ee80705ed7dc014096b` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_d78ab8ae6466.js` | 10108 | `70c26a3a7b86a5362b8d22f7abbe15fb22d01b21f11978b7dcb22933c30d7181` |
| `data/raw/defillama_adapter_evidence/aave-v3_index_master.js` | 18105 | `ab35fe5c071d0f691ef4b19320b1b942675cc5b539c32e5cf84a8ce5ba49e5ba` |
| `data/raw/defillama_adapter_evidence/commits_aave-v3_p1.json` | 286898 | `bb4cbf9f0828a6445c6b8f3f0a342339d9495c2183eeca61ffd50f83634f46c1` |
| `data/raw/defillama_adapter_evidence/commits_aave-v3_p2.json` | 5 | `2ba33ca0557f1bb5b7ba88d67f9d0093c7185a36ec51fe2b7bd9372d3e001d6d` |
| `data/raw/defillama_adapter_evidence/controller_yield.js` | 3340 | `f4403286d09fcd6fc514de505e893af4c77c5847fc50d5ee9a161e02a0af276f` |
| `data/raw/defillama_adapter_evidence/repo_tree_master.json` | 997876 | `5436edfb33f6d9a383c44eae2576ea4440fa1b598206b23716394ad2795b51fb` |
| `data/raw/defillama_adapter_evidence/serverless.yml` | 5967 | `515a26cb16d4272f077be37ca889df2c0511932c287604162766fc76fe6425bc` |
| `data/raw/defillama_adapter_evidence/triggerAdaptor.js` | 16389 | `c8f050882f68507f28f5e18e023699a6b01f71039489759833523e2d120f47c9` |
| `data/raw/defillama_adapter_evidence/yield-server_README.md` | 10529 | `a079c335cea26859d46e2f31304c8c25b6826630d2e90f0f6ad0b1316948b114` |
| `data/raw/hyperliquid/BTC_pages.ndjson` | 23412 | `ad1d9b8a5d6ce8908fd093574e75ad29e060849467279b7c5c0210a2e966586a` |
| `data/raw/hyperliquid/ETH_pages.ndjson` | 23806 | `edf03266cc0f6efc6e983d3ef4100ba3a563b4a499e318bf4f7f785a33272b48` |
| `data/raw/hyperliquid/BTC/page_0000.json` | 44939 | `83bc258aa86e192aee5c21bd27ec53a2acb9abda8924175453692d84829cceaa` |
| `data/raw/hyperliquid/BTC/page_0001.json` | 45075 | `a22f9e8ec4afae4347eafeb3ee3cfe907f0a893326c948b9ccbc11aa0ffab3d0` |
| `data/raw/hyperliquid/BTC/page_0002.json` | 45604 | `b5d1bdee38aad7f5b328c9e46c7ba0ee038b1ac0fe161decff8009a479c1b921` |
| `data/raw/hyperliquid/BTC/page_0003.json` | 45460 | `f62d2551ae8fef823cb5c904d8558d8aff79e6cd329fa9e492a9ec9f24183aaf` |
| `data/raw/hyperliquid/BTC/page_0004.json` | 44240 | `5d16143ddad4ebc5334e1251d6496a2b6b35197330730e8564aa511ba62c1153` |
| `data/raw/hyperliquid/BTC/page_0005.json` | 44167 | `db92219a6bb570321ba556af5b2fa9261719c9dab4f7b3beb8ec3ba6805152c4` |
| `data/raw/hyperliquid/BTC/page_0006.json` | 44700 | `1b1d3cc140dbc40af2a91060eb47c246aaa78661e52163176d1e207310912864` |
| `data/raw/hyperliquid/BTC/page_0007.json` | 44084 | `783fe8f68b7793100d6d0a813a548e0f4add0ba2dbf6fbca03c881e4ae91df4c` |
| `data/raw/hyperliquid/BTC/page_0008.json` | 44474 | `ac2dda04e813d3f1b33768778c5ba6c6cd91db525df39125a670b4ec3c090a2c` |
| `data/raw/hyperliquid/BTC/page_0009.json` | 44663 | `3e88d35b8ca162f366d277601b4de09772c23388288372d296822dfd0f500b63` |
| `data/raw/hyperliquid/BTC/page_0010.json` | 44425 | `bc7d64e96ff07c5356f937e130f9283300d22e2ca10c31bcff1b35924dd8209b` |
| `data/raw/hyperliquid/BTC/page_0011.json` | 44262 | `d205dcf439a4e05f87c77997003359adfe9ab6d4b9246834b1e3b5ffa62f2a8e` |
| `data/raw/hyperliquid/BTC/page_0012.json` | 44797 | `e5b2f9faecaa6f481bfc51b5989185856199b64e9ec9e5174642783ed58b81a0` |
| `data/raw/hyperliquid/BTC/page_0013.json` | 44432 | `0387690cbaf41d0202e987ffa2addde30b79437ac2e4de41d8ae6eaee8f3fc76` |
| `data/raw/hyperliquid/BTC/page_0014.json` | 44218 | `9784e07b812e010d783b1e25995d27b596dc942682a6a41a4c2edb48abdc1dd7` |
| `data/raw/hyperliquid/BTC/page_0015.json` | 44003 | `562bbb932e57b62839ef87bfabb796fb2be4b8a4c1389072f5b61366c023caa8` |
| `data/raw/hyperliquid/BTC/page_0016.json` | 44207 | `b75f3dc4046d001e28309358fa9ca3c3e6e8a9dd2bec42adb03ac286a2903afb` |
| `data/raw/hyperliquid/BTC/page_0017.json` | 44005 | `a22e30b0920db7f42789ce9d9d86f9f4bb0681d3c3d823e6571d5e9f83523f65` |
| `data/raw/hyperliquid/BTC/page_0018.json` | 44223 | `e276580553dd649858ed3dbd9e24c67f11ae47722cad28233df254e5083c99c0` |
| `data/raw/hyperliquid/BTC/page_0019.json` | 43958 | `5a5a91daa00568dc97cdf1ca24030a404c4738d6e3c202796caacc346e2e283c` |
| `data/raw/hyperliquid/BTC/page_0020.json` | 44029 | `132f5221be616a012f61df6475fe3847657637760f7899ee91c8062038ba8f64` |
| `data/raw/hyperliquid/BTC/page_0021.json` | 44205 | `53ba9e71c7c6d5089921be515c5824c63f83e9b0f3c9676847f83efec0a0bc31` |
| `data/raw/hyperliquid/BTC/page_0022.json` | 44084 | `c7690f615f38421764a58aabf731213d3a75a49ff52ace608d35107975a0c4ec` |
| `data/raw/hyperliquid/BTC/page_0023.json` | 43850 | `483a2fafd1b9b61caadf79234d9612ceec289c26b36460bedee7489acf538c29` |
| `data/raw/hyperliquid/BTC/page_0024.json` | 44595 | `f608bd82d496eb8dffa354c6d7a659889867f095efc9b5912c8340c221b1f4ac` |
| `data/raw/hyperliquid/BTC/page_0025.json` | 44540 | `80095a0cba60d3c1872cb4943abd881dccb14c136ad1ef30d9afbb3a79cdc9ee` |
| `data/raw/hyperliquid/BTC/page_0026.json` | 44034 | `db77103b69fd652507a533b5d7b7cb0bc3cc9e495d407a9d28ca562311baae8d` |
| `data/raw/hyperliquid/BTC/page_0027.json` | 44045 | `7c503f728b5a2b00f8e229736cf7719d71582df48568b203e1393aa590cfae90` |
| `data/raw/hyperliquid/BTC/page_0028.json` | 43824 | `2d16439194fa37a9e67de1ae45e96fb928a67d89ebdd4c904ac65c0fecc778a7` |
| `data/raw/hyperliquid/BTC/page_0029.json` | 44271 | `94082fd17d7da5838e664436f98c509b26d13a595e661ab5aa3f5976ddcfcd14` |
| `data/raw/hyperliquid/BTC/page_0030.json` | 44928 | `144b10b059502f2bc3421b1a5c0ea7ca39ac7248a4f1dd4491c00fccae3af786` |
| `data/raw/hyperliquid/BTC/page_0031.json` | 44556 | `c6cbe92447dc95510e8925af63beda3fc1f46360e6aeecfc805549ea562b14e0` |
| `data/raw/hyperliquid/BTC/page_0032.json` | 44403 | `9d15bfec1b37e4f2ba23e8f83f6e6cce0d198a479d87bf870446fdaaf94a2374` |
| `data/raw/hyperliquid/BTC/page_0033.json` | 44160 | `2af828265001d2da5982f921666c1dcd574a9aa9298ceb726df5c5ac06c671f6` |
| `data/raw/hyperliquid/BTC/page_0034.json` | 44292 | `1e6b16a00fe24e6c0473d3992a0a4c967b13fded3d6db2f413b40b7d08f4454d` |
| `data/raw/hyperliquid/BTC/page_0035.json` | 44314 | `95a439d497d0597f37da8ac36d5a68a97a1dfd268331757302f6cbf5a1073d12` |
| `data/raw/hyperliquid/BTC/page_0036.json` | 44340 | `7d7f069474ca34547c56da89bce1ab032d36ccc9cbca8dfead351ebc998a000e` |
| `data/raw/hyperliquid/BTC/page_0037.json` | 44236 | `ccfc58b9cbaae5187fdef9e069afac498e1947c83cced0edef61f2c097526ab0` |
| `data/raw/hyperliquid/BTC/page_0038.json` | 43863 | `44bc52d40be415054f54b322d72e4ceeb9deddcc8f864dd64d96e0aa1f7d498f` |
| `data/raw/hyperliquid/BTC/page_0039.json` | 44043 | `5346f51dff206b3afe7a5e3d937e8cfd444cc8ed739883f3f6189f9070ae67d4` |
| `data/raw/hyperliquid/BTC/page_0040.json` | 44291 | `3ed923e6dbd182a4a57049c6b7ff124baf7659b3232164a04e5aaee21dd2e962` |
| `data/raw/hyperliquid/BTC/page_0041.json` | 43896 | `27acc24a1db4c62d372fc51b559b12afad78cd521cb49480692d1d323021efb2` |
| `data/raw/hyperliquid/BTC/page_0042.json` | 44505 | `0408357e41acec8de7c8296e0b01cd90896a4c4811bae3a37db022876a4b91ac` |
| `data/raw/hyperliquid/BTC/page_0043.json` | 44866 | `45340eab5dd5b8f34b7aeb1182d7f7c29da8d6adc96e325e80273d0adea5989a` |
| `data/raw/hyperliquid/BTC/page_0044.json` | 44242 | `ed8cfdd5b2cfbff94cc85962e9b4534985a7d548a99d7f50d32dead6e8d76fd7` |
| `data/raw/hyperliquid/BTC/page_0045.json` | 44791 | `4385cb7d45e5f97bc759d9318f822475bf5784b73341d2871bda6f043ced2fa8` |
| `data/raw/hyperliquid/BTC/page_0046.json` | 45177 | `1f92b4ca32f66d1fad946e0bbda85620c0eaa2fa7d8f897ad43601d006cf0224` |
| `data/raw/hyperliquid/BTC/page_0047.json` | 45396 | `f54601739ae349d48c1cdd8c2c3e2bffe209dd0791e1b99156b053a2707b3e8d` |
| `data/raw/hyperliquid/BTC/page_0048.json` | 45273 | `37f710711d44f871da60be26a6da1ea48ca45a547e11ed3b1a1fc9a89865e0f5` |
| `data/raw/hyperliquid/BTC/page_0049.json` | 45421 | `b78b0c85b4b8e070ed9095cdfeb2bdb8c273eccf4c32eb19600f8946cb5253c7` |
| `data/raw/hyperliquid/BTC/page_0050.json` | 45166 | `17d94920b715234cea5af5780c665b90fef34364a3eaa5d7403db492974c5041` |
| `data/raw/hyperliquid/BTC/page_0051.json` | 44953 | `d1630651d6d6ecd3dbd79c5e2a2599175862e16dc3b30f50ea5dd47ba0b43d98` |
| `data/raw/hyperliquid/BTC/page_0052.json` | 45065 | `95c30c791e415e6cf0be54883680f829521cb9677d05faae313bda63ad77707d` |
| `data/raw/hyperliquid/BTC/page_0053.json` | 43945 | `65c213ce4d0aacf0bd16139bcf4ce90d2c5fbd04c463c84f4745ffa9a0576d7c` |
| `data/raw/hyperliquid/BTC/page_0054.json` | 44870 | `eefe8ce4bc8997f4f4a0380c0c6d12b75dc8979e63998424d0ffdbee37f2a7a3` |
| `data/raw/hyperliquid/BTC/page_0055.json` | 44285 | `ecb7dc2ebc5961a8830af2e2cde463da80777d8633223e4b3df60b64b0242a00` |
| `data/raw/hyperliquid/BTC/page_0056.json` | 44409 | `405ceacbab62c0e4976ebadde1a9e9fa2d61da19a9f948f99fc8fe7ba4bb580a` |
| `data/raw/hyperliquid/BTC/page_0057.json` | 44596 | `5bb80f2514af296bcd8907baf967b818ae6e44ca8262d49399e6dd5aeb24b12e` |
| `data/raw/hyperliquid/BTC/page_0058.json` | 39490 | `2244ef0954cab9c98e4ab3056108d22e6dd664232499b1298bbf91340ccc30c1` |
| `data/raw/hyperliquid/ETH/page_0000.json` | 44900 | `ab9477b4f26941aa3b609a36217dc9946c447f0232d411b0854e8e342b6c196a` |
| `data/raw/hyperliquid/ETH/page_0001.json` | 44870 | `f98bceae1deb28e5768134b95246a658d2ebcdc6ac3f0e3624a2f8b573addddd` |
| `data/raw/hyperliquid/ETH/page_0002.json` | 44974 | `35d940d2c4ffa2deb1b500ca60bb271e17aea8aae79525ed295cece9e3edecc1` |
| `data/raw/hyperliquid/ETH/page_0003.json` | 44853 | `00b7aa6ae309c759247139c1a3411994f00334529242efc151d24903a943f9c1` |
| `data/raw/hyperliquid/ETH/page_0004.json` | 44130 | `221d7eca7eece4eb599541caa8dfba5f46b67bff7098a98e86200eabdfe83648` |
| `data/raw/hyperliquid/ETH/page_0005.json` | 44398 | `26c2b756bf50ee2edefc94594d2ac0f652d481ae3b596fe29faa585c626f5e53` |
| `data/raw/hyperliquid/ETH/page_0006.json` | 44751 | `8f706e5dcd6c2df73a645dc9658cfc13d691f2322c2fbbe9fc899fc1a08265f4` |
| `data/raw/hyperliquid/ETH/page_0007.json` | 44365 | `23011b2a1242846e88006f1bef57f8bf6c6c70bd84e5e763542b4029787a695c` |
| `data/raw/hyperliquid/ETH/page_0008.json` | 44635 | `0d42c5b5ab7f0538d9b8ce77fc1c4e4e74a36482574ce3b34d955f19236b53c5` |
| `data/raw/hyperliquid/ETH/page_0009.json` | 44384 | `aa7acdd89f0505afd18595a26c0e98e430477ff6baf68809e79b5aff48ba3239` |
| `data/raw/hyperliquid/ETH/page_0010.json` | 44292 | `2df38466a97d5bc22d13d85f0bb0a533445f2190bda3f7ea0eaaa29016b5ea79` |
| `data/raw/hyperliquid/ETH/page_0011.json` | 44478 | `e253e2f6af350d4fbf1125487713c23ea80bb88a45c27652a307e4fb31dd9e93` |
| `data/raw/hyperliquid/ETH/page_0012.json` | 44784 | `3680422dda8dd70f548cd115bc568f11ee32d3d7d5d594a932d24d31557357e6` |
| `data/raw/hyperliquid/ETH/page_0013.json` | 44448 | `c20015a4d29888427571e7d8e522a2538bae67af2cfd6ac2ab7a615a1e18d7ce` |
| `data/raw/hyperliquid/ETH/page_0014.json` | 44063 | `29d81fbf879e589c381941bb5a0bea1ee823da5b533595ae8b11398238a6f69d` |
| `data/raw/hyperliquid/ETH/page_0015.json` | 44374 | `e1b665be20bbd8875e97b36d5766d1a36ac8ea5b87a531caaa449d62b787d096` |
| `data/raw/hyperliquid/ETH/page_0016.json` | 44418 | `1e882c089af8309cc8195f8a1376ee3c729464e06f5b115e6f6ccd338f387261` |
| `data/raw/hyperliquid/ETH/page_0017.json` | 44027 | `56ccacad71ac8e01fc7e1c0a98709e7b79c7afca3ec36ea8146d805e9786c482` |
| `data/raw/hyperliquid/ETH/page_0018.json` | 44119 | `b5213a64bccef1fc85f4541a40b91475f721319bcc4868eb1cd6f298cd1861a7` |
| `data/raw/hyperliquid/ETH/page_0019.json` | 44411 | `7a27144f1928f5222d7d93b998d64173e6fd1bcfcf2de871178bbd93bcd0319a` |
| `data/raw/hyperliquid/ETH/page_0020.json` | 44460 | `c04ebdf384dd99f42d155ec446cdfb780b56bd6da7ad5b72900bef8c4fc045aa` |
| `data/raw/hyperliquid/ETH/page_0021.json` | 44365 | `c0f62473ca47a6f98282b1e3bea350c65eca7fb0c23bd9a19242c7a49fda36f8` |
| `data/raw/hyperliquid/ETH/page_0022.json` | 44245 | `9e9a9c3e10cc3b2e34f8b6168dc4c1eb9b3edfbb58b12321f69beafc89eaf37f` |
| `data/raw/hyperliquid/ETH/page_0023.json` | 44075 | `170bb4c6722ebf9d18e5e535e572e14dbbfa694755f646dede47c39a4bb25d3d` |
| `data/raw/hyperliquid/ETH/page_0024.json` | 44694 | `00e0db709ce78cf1de45a1385aa6d37341a3198b703c4801968afadc89bb1b6c` |
| `data/raw/hyperliquid/ETH/page_0025.json` | 44617 | `08e3704ee8fd17d9b472d09e3e8d68bd3688bb8dc1cc8b0bfbaa00164e7e7b0c` |
| `data/raw/hyperliquid/ETH/page_0026.json` | 44100 | `696fdd8a1c332df0af86619aff978a3fd514138e1665a11f988dfd670526e610` |
| `data/raw/hyperliquid/ETH/page_0027.json` | 44039 | `ec9751103cf31ea9bce97ecf172d05dbef53f09a5b21d81ddef40c0972f73bd8` |
| `data/raw/hyperliquid/ETH/page_0028.json` | 44277 | `f7de54418ce3a11d7073e4ee92cbc8c2993316d9ed50268b1954f9a3b7943301` |
| `data/raw/hyperliquid/ETH/page_0029.json` | 44844 | `651186d6f2097565c6c5befdf1bf697431706dbe1d1395773ae7c2e8d58635f5` |
| `data/raw/hyperliquid/ETH/page_0030.json` | 45058 | `b10c2c281e559c57911d058d3e55baa9ac48f3ec4506c95c1aa9f5c272e6a566` |
| `data/raw/hyperliquid/ETH/page_0031.json` | 45564 | `b03abcb6fb2b8247c1b25ad032fcde19a9bf94964db700d6e103e8e5da47de6b` |
| `data/raw/hyperliquid/ETH/page_0032.json` | 44936 | `49d22fb033eaa9a881c7d5a79b22cdc8f79a7d3d8352b5c2b8e70eb69e9980e2` |
| `data/raw/hyperliquid/ETH/page_0033.json` | 44022 | `27f2c6081b19a8cd953ea8e1a6e1f2422d5a3bedeafec2ad4ceb0368f438f229` |
| `data/raw/hyperliquid/ETH/page_0034.json` | 44388 | `2711cf8e1a8422cd1cdb4e2191a0228ae496d8a456446820a09770adc4c61485` |
| `data/raw/hyperliquid/ETH/page_0035.json` | 44517 | `9191ab80a353e338ab236e31db9b3be0c9cf6e3ea7ce17b6b5ced91a4a808f8e` |
| `data/raw/hyperliquid/ETH/page_0036.json` | 44361 | `6fc6360b2eb7a624fb8044321421afb1fc80d1711dcd6b36a84820c9ed6f8313` |
| `data/raw/hyperliquid/ETH/page_0037.json` | 44424 | `caaeebf2853ed0d509b920f4b7e897673bbc03c0de96c93c3588628391252032` |
| `data/raw/hyperliquid/ETH/page_0038.json` | 44468 | `32661dba242d5563450b1e385f3571f67ce4148ef18530a5d7ea10040f7f54dd` |
| `data/raw/hyperliquid/ETH/page_0039.json` | 44285 | `0ad8ca737ded005732f62ea1e62ecc1f919ab613aa39a9358a09ec6aa12df524` |
| `data/raw/hyperliquid/ETH/page_0040.json` | 44479 | `b7727bbafdcf03839fabbca27eda8be21f6179f5780683c267d5b4c5a4ee2132` |
| `data/raw/hyperliquid/ETH/page_0041.json` | 44454 | `4a4b9491ccfb364a9d2a1911052fdbbd56fd16a96cb57ca3e9c0a095f36eecf1` |
| `data/raw/hyperliquid/ETH/page_0042.json` | 44239 | `0ed069098b6e208abe6136a1b6e21ed194572239e89d40a4b5c3136f1781085d` |
| `data/raw/hyperliquid/ETH/page_0043.json` | 44214 | `101db531dbd25530e742aa25d718b9187575f14d326613de95dace430ef03637` |
| `data/raw/hyperliquid/ETH/page_0044.json` | 44365 | `8c8b0648f4dc554b7d6320b1d4b0ebbedcea80ad59d2cae0138fa05106adab2f` |
| `data/raw/hyperliquid/ETH/page_0045.json` | 44715 | `a71de12400359640931adcb433014d3913d5eaa97794c4ac38add821b38bc220` |
| `data/raw/hyperliquid/ETH/page_0046.json` | 45084 | `945d746ee52c09960fcc17815cbbbdba3645d9079575f3e8c1041becbb4f8c13` |
| `data/raw/hyperliquid/ETH/page_0047.json` | 45223 | `1c5e413b590426bc8f6cc65d593a2d83ab5d97396d2c1b9f6d1f24c9dfa9655d` |
| `data/raw/hyperliquid/ETH/page_0048.json` | 45213 | `3be832ca78667d2222730f1b870b1ebba210d8356cc1475a1a8830bcb27f462b` |
| `data/raw/hyperliquid/ETH/page_0049.json` | 45502 | `60d1429038f60c7407769c8de8806f7efbfa48f21054a46add9331f3512e5c79` |
| `data/raw/hyperliquid/ETH/page_0050.json` | 44751 | `c1e3bdb7c4a066df1f0efc10cacb47bdca4572b8d941ddc90d4a3914cb6bde9a` |
| `data/raw/hyperliquid/ETH/page_0051.json` | 44745 | `41521d8ccd546f7dc63f4a35a3776f6dc4f6844786f08209ec53b1cbd70e5c4c` |
| `data/raw/hyperliquid/ETH/page_0052.json` | 44964 | `ff47b2e28169f4789e2a60acffb4f67fc5edd9700cb17372ab7fa0c17628e62c` |
| `data/raw/hyperliquid/ETH/page_0053.json` | 43747 | `6a19a83c0b8c75bfe319328a18cc50f4fe0360fed5b9aeb396b5710478176ccc` |
| `data/raw/hyperliquid/ETH/page_0054.json` | 44797 | `30a82a20c465083b33f5d7410f61ac0ebe13adab7dd7a7a36cfc7e37b76cd2ff` |
| `data/raw/hyperliquid/ETH/page_0055.json` | 44247 | `83b34e8f73ba50cfdd7a4dd3d601051325f118f66d7fe0a176bb75f2856c33a5` |
| `data/raw/hyperliquid/ETH/page_0056.json` | 44201 | `0d21512e5f65a9f8c35c8e7aab96fbf72f005dd1ae70ef4ae91933483555b501` |
| `data/raw/hyperliquid/ETH/page_0057.json` | 44147 | `b5a254a222eafac72cab348270ac1922eafe6fc056d59ab96f24c02c9df949c5` |
| `data/raw/hyperliquid/ETH/page_0058.json` | 39826 | `b7c814db668b13dcdf8a29fd3df81eb6240dae73d2dbcc56b2e4ff126a58ccb4` |
| `data/raw/hyperliquid/ETH/page_0059.json` | 92 | `8b978e749944d6e2b322ea8f0bd73936ffc2340c48d825077d557d65fd11845b` |
| `data/source_consistency/V1_DESIGN.md` | 32236 | `8e5010524e7b34c0c89bfe758067ef92db6ee52db682f23eae87ef09bd657e32` |
| `frozen_rules/STUDY0_RULES.md` | 3459 | `692b32814eafdc585068af6eeb440c337682d1e5affc7cc6d9b28ed6af02ed03` |
| `frozen_rules/study0.json` | 8658 | `3b7d361a3e0467c3aadd8b092ff56e2d0c8a22556ad8699133e7e5a2212cf370` |
| `study/CHANGELOG.md` | 3274 | `5ddf03e72f00592f65c038a470f183a130e76fa02a48af855b5047c36e147c43` |
| `study/DIRECTOR_DECISIONS_PRESEAL.md` | 4074 | `c8e34bce31d21fb06a2aa2db7dedbdffd71914288a0d86ef89ea71a0c35b25ad` |
| `study/DIRECTOR_DECISION_S6_RATE_CONVENTION.md` | 2051 | `cd73b696894c7e2c9fb56dc278e83420c93649061c6749146a9f30a4ec856810` |
| `study/ENVIRONMENT.md` | 2871 | `14fd824bdbadcf5634d23ad9b99427008dbf1dfc994a070380144aff788e6fa9` |
| `study/SEAL_RECORD.md` | 2049 | `af9215c25a57905f6ffb518f12887ddb046228abe234305bf6d735ba7af5b8cb` |
| `study/commit_requests/COMMIT_REQUEST_001_DESIGN_SEAL.md` | 3317 | `d59aff0669718a781e2a4d2884525d09de88d16c315b22c416d336db18129599` |
| `study/host_receipts/HOST_RECEIPT_001_DESIGN_SEAL.md` | 1337 | `fa351fc02737a14193bd9d8ff5209fdd25deeb42609975eb444e1ead9de01170` |
| `study/prompts/amendments/AMENDMENT_A1_A2.txt` | 2267 | `9c755cd5826e03e28845d4d6328bef9136460cf1c5cffb3878bb2d3599364cd6` |
| `study/prompts/original/STUDY_0_AUDITOR_PROMPT.txt` | 15876 | `fea411aef5c3cd321a0b3a4cf84cd234868e9c59938ea5e0799e4196980283ff` |
| `study/prompts/original/STUDY_0_BUILDER_PROMPT.txt` | 15774 | `ffdde616794b48665ae3b0cfd938e9eb75228956bbe424bc59eef9563ff5642c` |
| `study/prompts/working/A3_A4_BLOCK.txt` | 4255 | `23ca07391bcf55bb6670aa02f7704a5a5e8509d0da47566928649eb90a009e87` |
| `study/prompts/working/APPENDED_AMENDMENTS_BLOCK.txt` | 6522 | `3857fd772ad5f6e58a65bde3a7c8ec434d1f3545f6026b4011385527481fb1f4` |
| `study/prompts/working/PROMPT_COMPARISON.md` | 2206 | `8bf4dd7554b8a916445e14fc177361ac5f7ecc45f227818cbc851f7d927d9a0a` |
| `study/prompts/working/STUDY_0_AUDITOR_PROMPT.txt` | 22398 | `1238ade3736034f720ddc95d072a34fe9f1fbf77e1892547204928d496aa093b` |
| `study/prompts/working/STUDY_0_BUILDER_PROMPT.txt` | 22296 | `58f386167c0fd24fcfa9a1bf202fb4627d9265800cfcfc3bdad4d510798fd86d` |
| `study/src/build_manifest.py` | 1993 | `2d5a32c29c25f42578def031039c5d18fb66a13227c2b14e97fe25c23a4b38ea` |
| `study/src/compute_study0.py` | 26270 | `184af1ecd73b588ec9c024f9c20309395f4f355d5421fa54830528d7343b3501` |
| `study/src/independent_check.py` | 3979 | `734e159db9cd72fb2bb26945375329fe07708d0238ee6f95184c86557c5e705b` |
| `study/src/inventory_preseal.py` | 4943 | `02d5f9d5d3b5862e10af699800b6643483817d88ee22aba401177e93a5acbfbc` |
| `study/src/retrieve_adapter_evidence.sh` | 1167 | `7c74efa0c631c48814c3487f51961cdd7ebaa1abd1d3eabef2f3d51ea12a73de` |
| `study/src/retrieve_adapter_history.sh` | 781 | `4af49485400b1aeef25a771c41e939fc76301046414cac93e20486d354de0e35` |
| `study/src/retrieve_coinbase.py` | 2807 | `ee22e297bd3d31f3185226c6d193df88608f835a478bf7aa37f4badc08850b41` |
| `study/src/retrieve_defillama.sh` | 713 | `9e6a960c8424ba973e7245bd2e1259351f0c6bf802a481b531ac41aa1c51c516` |
| `study/src/retrieve_hyperliquid.py` | 3241 | `4a10c238061081624c28d030e6d2da17d7e9e9c6a52fbe456f26aff54ba66cff` |
| `study/src/test_fixtures.py` | 8767 | `50e00e3bd55cc0d965925b69f0d0a8c1f95dad37a0e681dc9d71664d1f913803` |

End of request. The builder stops at this boundary; no Study 0 result computation
occurs until the coordinator reports this commit and the run results.
