# TF::TencentCloud::CdnDomain HttpsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#http2switch" title="Http2Switch">Http2Switch</a>" : <i>String</i>,
    "<a href="#httpsswitch" title="HttpsSwitch">HttpsSwitch</a>" : <i>String</i>,
    "<a href="#ocspstaplingswitch" title="OcspStaplingSwitch">OcspStaplingSwitch</a>" : <i>String</i>,
    "<a href="#spdyswitch" title="SpdySwitch">SpdySwitch</a>" : <i>String</i>,
    "<a href="#verifyclient" title="VerifyClient">VerifyClient</a>" : <i>String</i>,
    "<a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>" : <i>[ <a href="clientcertificateconfigdefinition.md">ClientCertificateConfigDefinition</a>, ... ]</i>,
    "<a href="#forceredirect" title="ForceRedirect">ForceRedirect</a>" : <i>[ <a href="forceredirectdefinition.md">ForceRedirectDefinition</a>, ... ]</i>,
    "<a href="#servercertificateconfig" title="ServerCertificateConfig">ServerCertificateConfig</a>" : <i>[ <a href="servercertificateconfigdefinition.md">ServerCertificateConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#http2switch" title="Http2Switch">Http2Switch</a>: <i>String</i>
<a href="#httpsswitch" title="HttpsSwitch">HttpsSwitch</a>: <i>String</i>
<a href="#ocspstaplingswitch" title="OcspStaplingSwitch">OcspStaplingSwitch</a>: <i>String</i>
<a href="#spdyswitch" title="SpdySwitch">SpdySwitch</a>: <i>String</i>
<a href="#verifyclient" title="VerifyClient">VerifyClient</a>: <i>String</i>
<a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>: <i>
      - <a href="clientcertificateconfigdefinition.md">ClientCertificateConfigDefinition</a></i>
<a href="#forceredirect" title="ForceRedirect">ForceRedirect</a>: <i>
      - <a href="forceredirectdefinition.md">ForceRedirectDefinition</a></i>
<a href="#servercertificateconfig" title="ServerCertificateConfig">ServerCertificateConfig</a>: <i>
      - <a href="servercertificateconfigdefinition.md">ServerCertificateConfigDefinition</a></i>
</pre>

## Properties

#### Http2Switch

HTTP2 configuration switch. Valid values are `on` and `off`. and default value is `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsSwitch

HTTPS configuration switch. Valid values are `on` and `off`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspStaplingSwitch

OCSP configuration switch. Valid values are `on` and `off`. and default value is `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpdySwitch

Spdy configuration switch. Valid values are `on` and `off`. and default value is `off`. This parameter is for white-list customer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyClient

Client certificate authentication feature. Valid values are `on` and `off`. and default value is `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateConfig

_Required_: No

_Type_: List of <a href="clientcertificateconfigdefinition.md">ClientCertificateConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceRedirect

_Required_: No

_Type_: List of <a href="forceredirectdefinition.md">ForceRedirectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateConfig

_Required_: No

_Type_: List of <a href="servercertificateconfigdefinition.md">ServerCertificateConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

