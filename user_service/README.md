(.venv) andrey@andrey-BoDE-WXX9:~/PycharmProjects/system_design_task_05/user_service$ wrk -t1 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    35.73ms   43.90ms 415.56ms   91.82%
    Req/Sec   377.40    175.37   600.00     63.64%
  3723 requests in 10.01s, 672.61KB read
Requests/sec:    371.85
Transfer/sec:     67.18KB
(.venv) andrey@andrey-BoDE-WXX9:~/PycharmProjects/system_design_task_05/user_service$ wrk -t5 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    31.33ms   40.26ms 394.63ms   91.76%
    Req/Sec    88.87     35.75   131.00     78.10%
  4306 requests in 10.02s, 777.94KB read
Requests/sec:    429.74
Transfer/sec:     77.64KB
(.venv) andrey@andrey-BoDE-WXX9:~/PycharmProjects/system_design_task_05/user_service$ wrk -t10 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    24.39ms   20.74ms 232.24ms   92.61%
    Req/Sec    47.17     13.70    70.00     82.42%
  4660 requests in 10.01s, 841.89KB read
Requests/sec:    465.41
Transfer/sec:     84.08KB

========================================================================================================

(.venv) andrey@andrey-BoDE-WXX9:~/PycharmProjects/system_design_task_05/user_service$ wrk -t1 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.61ms    4.34ms  54.94ms   93.13%
    Req/Sec     1.41k   228.79     1.66k    85.00%
  14076 requests in 10.00s, 2.48MB read
Requests/sec:   1407.01
Transfer/sec:    254.21KB
(.venv) andrey@andrey-BoDE-WXX9:~/PycharmProjects/system_design_task_05/user_service$ wrk -t5 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.52ms    3.70ms  42.68ms   92.92%
    Req/Sec   280.70     48.66   340.00     76.20%
  13980 requests in 10.01s, 2.47MB read
Requests/sec:   1396.80
Transfer/sec:    252.35KB
(.venv) andrey@andrey-BoDE-WXX9:~/PycharmProjects/system_design_task_05/user_service$ wrk -t10 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     8.26ms   10.27ms 153.77ms   95.99%
    Req/Sec   143.11     21.48   171.00     82.04%
  14179 requests in 10.01s, 2.50MB read
Requests/sec:   1415.83
Transfer/sec:    255.80KB

