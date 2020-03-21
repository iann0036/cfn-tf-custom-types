# Terraform::AzureRM::ApplicationGateway BackendHttpSettings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#affinitycookiename" title="AffinityCookieName">AffinityCookieName</a>" : <i>String</i>,
    "<a href="#cookiebasedaffinity" title="CookieBasedAffinity">CookieBasedAffinity</a>" : <i>String</i>,
    "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#pickhostnamefrombackendaddress" title="PickHostNameFromBackendAddress">PickHostNameFromBackendAddress</a>" : <i>Boolean</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#probename" title="ProbeName">ProbeName</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#requesttimeout" title="RequestTimeout">RequestTimeout</a>" : <i>Double</i>,
    "<a href="#trustedrootcertificatenames" title="TrustedRootCertificateNames">TrustedRootCertificateNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#authenticationcertificate" title="AuthenticationCertificate">AuthenticationCertificate</a>" : <i>[ <a href="backendhttpsettings-authenticationcertificate.md">AuthenticationCertificate</a>, ... ]</i>,
    "<a href="#connectiondraining" title="ConnectionDraining">ConnectionDraining</a>" : <i>[ <a href="backendhttpsettings-connectiondraining.md">ConnectionDraining</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#affinitycookiename" title="AffinityCookieName">AffinityCookieName</a>: <i>String</i>
<a href="#cookiebasedaffinity" title="CookieBasedAffinity">CookieBasedAffinity</a>: <i>String</i>
<a href="#hostname" title="HostName">HostName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#pickhostnamefrombackendaddress" title="PickHostNameFromBackendAddress">PickHostNameFromBackendAddress</a>: <i>Boolean</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#probename" title="ProbeName">ProbeName</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#requesttimeout" title="RequestTimeout">RequestTimeout</a>: <i>Double</i>
<a href="#trustedrootcertificatenames" title="TrustedRootCertificateNames">TrustedRootCertificateNames</a>: <i>
      - String</i>
<a href="#authenticationcertificate" title="AuthenticationCertificate">AuthenticationCertificate</a>: <i>
      - <a href="backendhttpsettings-authenticationcertificate.md">AuthenticationCertificate</a></i>
<a href="#connectiondraining" title="ConnectionDraining">ConnectionDraining</a>: <i>
      - <a href="backendhttpsettings-connectiondraining.md">ConnectionDraining</a></i>
</pre>

## Properties

#### AffinityCookieName

The name of the affinity cookie.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieBasedAffinity

Is Cookie-Based Affinity enabled? Possible values are `Enabled` and `Disabled`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

Host header to be sent to the backend servers. Cannot be set if `pick_host_name_from_backend_address` is set to `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Backend HTTP Settings Collection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The Path which should be used as a prefix for all HTTP requests.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PickHostNameFromBackendAddress

Whether host header should be picked from the host name of the backend server. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port which should be used for this Backend HTTP Settings Collection.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbeName

The name of an associated HTTP Probe.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The Protocol which should be used. Possible values are `Http` and `Https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestTimeout

The request timeout in seconds, which must be between 1 and 86400 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedRootCertificateNames

A list of `trusted_root_certificate` names.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationCertificate

_Required_: No

_Type_: List of <a href="backendhttpsettings-authenticationcertificate.md">AuthenticationCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionDraining

_Required_: No

_Type_: List of <a href="backendhttpsettings-connectiondraining.md">ConnectionDraining</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

