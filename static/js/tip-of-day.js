const tipEl = document.getElementById("tip-of-the-day");

if (tipEl) {
  const petTips = [
    "🐶 Dogs can learn more than 100 words and gestures.",
    "🐱 Cats use their whiskers to judge spaces and movement.",
    "🐾 Regular grooming helps you spot skin issues early.",
    "🦴 A tired dog is usually a happier dog.",
    "🐈 Cats often blink slowly to show trust and comfort.",
    "🩺 Preventive care is easier than emergency care.",
    "💧 Fresh water should always be available for pets.",
    "🐕 Walks are great for both exercise and mental stimulation.",
    "🐾 Keeping pet records in one place saves stress later.",
    "🐶 Dogs can read human emotions from facial expressions.",
    "🐱 Most cats sleep between 12 and 16 hours a day.",
    "🐾 Short daily checks can help you notice health changes early.",
    "🐶 A dog’s nose print is unique, like a fingerprint.",
    "🐱 Cats often rub against you to mark you as part of their safe space.",
    "🦷 Dental care matters for pets too, not just humans.",
    "🐕 Sniffing during walks is mental exercise for dogs.",
    "🐈 A slow blink from a cat is often called a kitty kiss.",
    "💉 Keeping vaccines up to date helps prevent serious illness.",
    "🐾 Grooming is also a good time to check paws, ears, and skin.",
    "🐶 Some dogs can learn routines faster than individual commands.",
    "🐱 Cats can rotate their ears to track sounds more precisely.",
    "🩺 Preventive care saves stress, time, and often money later.",
    "💧 Hydration matters more than many pet owners realize.",
    "🐕 Dogs often use body language before they bark or growl.",
    "🐈 Indoor cats still benefit from play that mimics hunting.",
    "🐾 A small habit tracker can make pet care much easier.",
    "🐶 Dogs can pick up on your mood and energy.",
    "🐱 Whiskers are touch-sensitive tools, not just cute decorations.",
    "🦴 Chewing can help dogs relax and stay mentally engaged.",
    "🐾 Consistency helps pets feel safer and more confident.",
    "🐶 Puppies are born deaf, blind, and toothless.",
    "🐱 Cats often prefer several small meals rather than one big one.",
    "🪮 Brushing can reduce shedding and help prevent matting.",
    "🐕 Enrichment is just as important as exercise.",
    "🐈 Cats love routines and notice changes quickly.",
    "🩺 Recording symptoms before a vet visit can be really helpful.",
    "💧 Clean bowls and fresh water should be part of the daily routine.",
    "🐾 Nail trims are easier when done regularly.",
    "🐶 Dogs dream during REM sleep, just like humans.",
    "🐱 Cats use scent as a huge part of how they understand the world.",
    "🐕 Training works best when it is short, calm, and consistent.",
    "🐈 Scratching is normal cat behavior, not bad behavior.",
    "🦷 Bad breath in pets is not always normal and can signal dental issues.",
    "🐾 Pet records in one place make emergencies less chaotic.",
    "🐶 If a dog sleeps touching you, it usually sees you as safe.",
    "🐱 Many cats prefer high spots because they feel secure there.",
    "🩺 It is easier to notice patterns when appointments are logged properly.",
    "💤 Rest is part of health too, especially for growing pets.",
    "🐕 Different breeds often have very different energy needs.",
    "🐈 Play helps indoor cats stay active, curious, and less bored.",
    "🐾 Small daily care tasks prevent bigger problems later.",
    "🐶 Tail wagging does not always mean a dog is friendly — context matters.",
    "🐱 Cats can make over 100 different vocal sounds.",
    "🦴 Rotating toys can make old toys feel new again.",
    "💧 Some pets prefer wider bowls, especially cats.",
    "🐕 A bored dog may invent its own job at home.",
    "🐈 Hiding can be a sign a cat is stressed or unwell.",
    "🩺 Noticing changes in appetite is often important.",
    "🐾 Healthy routines make pet care feel less overwhelming.",
    "🐶 Dogs often understand tone before they understand words.",
    "🐱 Purring can mean comfort, but sometimes also self-soothing.",
    "🪥 Getting pets used to handling early makes care easier later.",
    "🐕 Mental stimulation can tire a dog almost as much as physical exercise.",
    "🐈 Cats usually prefer clean litter boxes and quiet spaces.",
    "🐾 Keeping notes helps you remember the little things.",
    "🐶 Some dogs sneeze during play to show they are only joking around.",
    "🐱 Cats often communicate with their tail position.",
    "💧 Water fountains can encourage some pets to drink more.",
    "🐕 Rewarding calm behavior is just as important as correcting chaos.",
    "🐈 Cats may knead when they feel safe and content.",
    "🩺 A wellness check is useful even when everything seems fine.",
    "🐾 Prevention is the least dramatic form of love."
  ];

  let tipIndex = 0;

  function showNextTip() {
    tipEl.style.opacity = "0";

    setTimeout(() => {
      tipEl.textContent = petTips[tipIndex];
      tipEl.style.opacity = "1";
      tipIndex = (tipIndex + 1) % petTips.length;
    }, 250);
  }

  showNextTip();
  setInterval(showNextTip, 30000);
}