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

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieBasedAffinity

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PickHostNameFromBackendAddress

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbeName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestTimeout

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedRootCertificateNames

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

