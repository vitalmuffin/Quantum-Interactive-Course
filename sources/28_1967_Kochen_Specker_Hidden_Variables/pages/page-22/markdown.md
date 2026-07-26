QUANTUM MECHANICS

79

Using the orthogonality of $Q$ and $P_{\sigma(A)}$, we have

$$\sin \rho \sin \theta \cos \varphi_\theta + \cos \rho \cos \theta = 0$$

or

$$\varphi_\theta = \cos^{-1} (-\cot \rho \cot \theta).$$

Thus

$$\frac{1}{2}(1 + \cos \rho) = 2 \int_{\rho - \pi/2}^{\pi/2} u(\theta) \sin \theta \cos^{-1} (-\cot \rho \cot \theta) \, d\theta.$$

Letting $x = \rho - \pi/2$, we have

$$\frac{1}{2}(1 - \sin x) = -2 \int_{\pi/2}^{x} u(\theta) \sin \theta \cos^{-1} (\cot \theta \tan x) \, d\theta.$$

Now, differentiating both sides with respect to $x$, we obtain

$$-\frac{1}{2} \cos x = -2u(x) \sin x \cos^{-1} (\cot x \tan x) + \int_{\pi/2}^{x} \frac{u(\theta) \sin \theta \cot \theta \sec^2 x}{(1 - \cot^2 \theta \tan^2 x)^{1/2}} \, d\theta$$

or,

$$\cos^2 x = -4 \int_{\pi/2}^{x} \frac{u(\theta) \cos \theta}{(1 - \cot^2 \theta \tan^2 x)^{1/2}} \, d\theta.$$

If we set $z = \cos^2 x$, $s = \cos^2 \theta$, and $w(s) = u(\theta)$, we find

$$z = \int_0^s \frac{2w(s)}{(s - s)^{1/2}} \, ds.$$

This is a special case of Abel's integral equation, and is easily solved by Laplace transforms. Namely, if $*$ denotes convolution and $L(f) = \int_0^\infty f(x)e^{-tx} \, dx$, the Laplace transform, then

$$z = w * 2z^{-1/2}.$$

Hence,

$$L(z) = L(w)L(2z^{-1/2}),$$

or

$$\begin{aligned} L(w) &= L(z)/L(2z^{-1/2}) \\ &= \frac{1}{2\sqrt{\pi}} t^{-3/2} \\ &= L((1/\pi)s^{1/2}), \end{aligned}$$

so that

$$w(s) = (1/\pi)s^{1/2}.$$

This content downloaded from 140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC All use subject to https://about.jstor.org/terms