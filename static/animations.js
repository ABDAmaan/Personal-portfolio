let observer = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        // Start typing
        const typewriter = new Typewriter("#typewriter", {
          loop: false,
          delay: 75,
        });

        typewriter
          .pauseFor(1000)
          .typeString(">> I don’t know who you are.")
          .pauseFor(1000)
          .typeString("<br>>> I don’t know what you’re looking for.")
          .pauseFor(1000)
          .typeString(
            "<br>>> But what I do have are a very particular set of skills."
          )
          .pauseFor(1000)
          .typeString(
            "<br>>> Skills I’ve built over years of designing, coding, and solving."
          )
          .pauseFor(1000)
          .typeString(
            "<br>>> Skills that make me a nightmare for bugs and broken systems."
          )
          .pauseFor(1000)
          .typeString(
            "<br>>> If you’re here to build something meaningful — we’ll get along just fine."
          )
          .pauseFor(1000)
          .typeString(
            "<br>>> But if you’re here with outdated CSS and no version control…"
          )
          .pauseFor(1000)
          .typeString("<br>>> <span style='color:#f64c72;'>I will</span>")
          .pauseFor(1000)
          .typeString("<span style='color:#f64c72;'> refactor you.</span>")
          .start();

        observer.unobserve(entry.target); // Only run once
      }
    });
  },
  {
    threshold: 0.5, // Trigger when 50% of the element is visible
  }
);

// Observe the typewriter element
const typewriterTarget = document.getElementById("typewriter");
observer.observe(typewriterTarget);
