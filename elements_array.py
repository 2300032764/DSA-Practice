<!DOCTYPE html>
<html lang="en">

<head>
    <link rel="icon" href="https://www.codechef.com/favicon.ico" type="image/x-icon"/>
    <title>Search an element in an array Practice Problem in Arrays</title>
    <meta charset="utf-8"/>
    <meta name="description" content='Test your Arrays knowledge with our Search an element in an array practice problem.  Dive into the world of arrays challenges at CodeChef.'/>
    <meta name="og:image" content="https://cdn.codechef.com/sites/all/themes/abessive/cc-logo.png"/>
    <meta name="og:type" content="website"/>
    <meta name="theme-color" content="#000000"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.codechef.com/practice/course/arrays/ARRAYS/problems/SEARCHINARR">
    <script src="https://accounts.google.com/gsi/client" async></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="prefetch" href="https://cdn.codechef.com/images/cc-logo.svg" as="image" type="image/svg+xml">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700;800&family=Roboto+Mono:wght@100;300;400;500;700&family=Fustat:wght@100;200;300;400;500;600;700;800;900&display=swap"
          rel="stylesheet">

    <!-- Initial loader classes -->
  <style>
    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

    .loadingIcon {
      border: 0.4em solid rgba(0, 0, 0, 0.0);
      border-top: 0.4em solid #2A67B1;
      border-radius: 50%;
      width: 4em;
      height: 4em;
      animation: spin 1s linear infinite;
      color: #2A67B1;
    }

    .loading {
      width: 100%;
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: rgb(108, 116, 134);
      background: inherit;
      z-index: 100;
      position: absolute;
    }

    .message {
      padding: 16px;
      text-align: center;
      font-family: sans-serif;
    }

    /* Dark Mode styles */
    .loader-icon-dark {
      border-top: 0.4em solid #5780b0;
    }
    .dark {
      background: #1d1e23;
      color: rgb(255 255 255 / 60%);
    }
  </style>
  <script>

    const languageIdeRoutes = [
      'python', 'java', 'cpp', 'c', 'pypy', 'csharp', 'javascript', 'go', 'php', 'kotlin', 'rust', 'r', 'sql', 'html',
      'oracledb', 'react'
    ];

    // workbench.js is 2.8MB and loaded lazily by LabEditor. Fetching it early on the skill-test
    // page (via idle fetch instead of <link rel="prefetch"> which returns 503 on staging/prod)
    // warms the HTTP cache before the React component requests it.
    if (/^\/skill-test\/[^/]+/.test(window.location.pathname)) {
      window.addEventListener('load', () => {
        const kick = () => {
          fetch('/build/vscode/static/out/vs/code/browser/workbench/workbench.js', {
            credentials: 'include',
            priority: 'low'
          }).catch(() => {});
        };
        ('requestIdleCallback' in window) ? requestIdleCallback(kick) : setTimeout(kick, 1000);
      });
    }

    if (
      (['faq', 'pro', 'contests'].includes(window.location.pathname.split('/').filter(Boolean).pop())) ||
      (['learn', 'games', 'viewsolution',
        'submit', 'practice', 'dashboard', 'getting-started', 'college-program', 'practice-old',
        'roadmap', 'blogs', 'roadmaps', 'blogs', 'skill-tests', 'ide', 'mobile'
      ].includes(window.location.pathname.split('/').filter(Boolean)[0])) ||
      (['submit'].includes(window.location.pathname.split('/').filter(Boolean)[1])) ||
      (['status'].includes(window.location.pathname.split('/').filter(Boolean).slice(-2, -1).pop())) || [
        // Regex to match the practice and contest submit routes
        /^\/(submit\/([A-Z]+[A-Z0-9_]*)+|problems\/([A-Z]+[A-Z0-9_]*)+|([A-Z]+[A-Z0-9_]*)+\/submit\/([A-Z]+[A-Z0-9_]*)+|([A-Z]+[A-Z0-9_]*)+\/problems\/([A-Z]+[A-Z0-9_]*)+)$/
      ].some((regexp) => (regexp.test(window.location.pathname))) ||
      (languageIdeRoutes.some(lang => window.location.pathname.includes(`${lang}-online-compiler`)))
    ) {
      const metaElement = document.createElement('meta');
      metaElement.setAttribute('name', 'viewport');
      metaElement.setAttribute('content', 'width=device-width, initial-scale=1');
      document.head.appendChild(metaElement);
    }

    (function (w, d, s, l, i) {
      w[l] = w[l] || [];
      w[l].push({
        'gtm.start': new Date().getTime(),
        event: 'gtm.js'
      });
      var f = d.getElementsByTagName(s)[0],
        j = d.createElement(s),
        dl = l != 'dataLayer' ? '&l=' + l : '';
      j.async = true;
      j.src =
        'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
      f.parentNode.insertBefore(j, f);
    })(window, document, 'script', 'dataLayer', 'GTM-TV5X2M');
  </script>
  <script type="module" crossorigin src="/build/react2/assets/index-CdK_-Anu.js"></script>
  <link rel="modulepreload" crossorigin href="/build/react2/assets/__commonjsHelpers__-BosuxZz1.js">
  <link rel="modulepreload" crossorigin href="/build/react2/assets/vendor-mui-DaEQ2xI4.js">
  <link rel="modulepreload" crossorigin href="/build/react2/assets/vendor-sweetalert2-CokzRhbv.js">
  <link rel="stylesheet" crossorigin href="/build/react2/assets/index-JiPqnELE.css">
</head>

<body style="background:#1d1e23;">
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="initialLoadingComponent" class="loading fullPage notranslate dark">
    <div class="loadingIcon loader-icon-dark"></div>
    <span id="initialLoadingMessage" class="message dark"></span>
  </div>
  <div id="root"></div>
  <script>
    // Payment Scripts
    if (['pro', 'getting-started', 'dashboard', 'roadmap'].includes(window.location.pathname.split('/')[1])) {
      const razorPay = document.createElement('script');
      razorPay.setAttribute('src', 'https://checkout.razorpay.com/v1/checkout.js');
      document.head.appendChild(razorPay);

      // const instamojo = document.createElement('script');
      // instamojo.setAttribute('src', 'https://js.instamojo.com/v1/checkout.js');
      // document.head.appendChild(instamojo);

    }
    const scriptElement = document.createElement('script');
    scriptElement.setAttribute('src',
            "/sites/all/modules/codechef_alerts/codechef_alerts.js?v=649c43b6894169b33b5557aa0374459d"
    );
    scriptElement.setAttribute('async', '');
    document.body.appendChild(scriptElement);
  </script>
  <script type="text/javascript" async
    src="/sites/all/themes/mallow/src/js/cookies.js?v=c0c952b5f5af42bd78098f00c77cfa63"></script>
  <script>
    const loadingMessages = [
      'Transform every day with the habit of learning',
      'Explored our courses yet? Enroll now! Over 500k learners have already enrolled.',
      'Pro tip: Facing a challenge while solving problem? Tap into AI Help',
      'Set the pace, set the goal, Maintain your streak by solving problem everyday',
      'Set your own goal to finish each modules',
      'Pro tip: Pseudo code first, then code with ease.',
      'Coding is not difficult, you need to try hard enough',
      '1% better everyday can lead to big results.',
      'Hard work and consistency is the only way to success',
      'Don\'t stop until you are in the top 1%',
      'Becoming the best coder is easy! Just keep doing CodeChef.',
      'Compete in the XP Weekly Leaderboard and see where you rank!',
    ];
    const randomIndex = Math.floor(Math.random() * loadingMessages.length);
    document.getElementById('initialLoadingMessage').innerText = loadingMessages[randomIndex];
  </script>
</body>

</html>
<script>
    window.CDN_URL = 'https://cdn.codechef.com';
    window.csrfToken = "bff86193ef113380af7cf2fb69ea3ca7b206edbcc5e6bd4d05887d66a13ba203";
    window.APPS_URL = 'https://www.codechef-apps.com';
    window.DISCUSS_URL = 'https://discuss.codechef.com';
    window.tawkPropertyId = '668d037a7a36f5aaec9634a5';
    window.widgetId = '1i2bdb6dt';
    try {
        window.codeChefUserData = {"status":"success","user":{"username":"kl_2300032764","uid":"4882284","email":"2300032764@kluniversity.in","profileImage":null,"profileImagePath":"https:\/\/cdn.codechef.com\/sites\/all\/themes\/abessive\/images\/user_default_thumb.jpg","oauth_buttons":null,"oauthData":null,"html_handle":"<span \n            class='rating' \n            style='display: inline-block; \n                    font-size: 10px; \n                    background: #666666;\n                    padding: 0 3px; \n                    line-height: 1.3; \n                    color: white;\n                    margin-right: 2px;'>1&#9733;<\/span><span class='m-username--link'>kl_2300032764<\/span>","userRatingStar":1,"userRatingStarColor":"#666666","isAdmin":false,"isCollegeOfferingAdmin":false,"isHYCAdmin":false,"hasAnySpecialPermission":false,"isPremiumUser":true,"isVerifiedUser":true,"user_consented_privacy_policy_version":"9721896","user_consented_privacy_policy_on":"2025-02-24 19:46:45","current_privacy_policy_version":null,"visitedContests":[],"rating":1238,"userStarHtml":"<span class='m-user-star' style='background:#666666;'>1&nbsp;&#9733;<\/span>","proDiscount":null,"theme":"dark","fullName":"yuthi_7976","pro_plan":"trial","sale":{"saleEndDateIST":"2026-04-30T05:59:59","saleTitle":"FLASH SALE","saleDescription":"CODECHEF FLASH SALE IS ACTIVE","isSaleOngoing":false,"saleDaysLeft":-2,"saleEndDateUTC":"2026-04-30T00:29:59"},"isUserPartOfAnyUserGroup":true,"userSelectedProgrammingLanguage":"PYTH 3","country":"India","isNumberVerified":false,"isJobProfileComplete":false,"league":4,"credits":0,"aiChatLanguage":"English"},"time":1777717459,"ip":"223.187.60.147","adStrip":null};
    } catch (e) {
        window.codeChefUserData = {};
    }
    try {
        window.userMessages = {"status":"success","messages":null};
    } catch (e) {
        window.userMessages = {};
    }
</script>
