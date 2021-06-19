# TF::Volterra::AwsTgwSite TlsInterceptDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enableforalldomains" title="EnableForAllDomains">EnableForAllDomains</a>" : <i>Boolean</i>,
    "<a href="#trustedcaurl" title="TrustedCaUrl">TrustedCaUrl</a>" : <i>String</i>,
    "<a href="#volterracertificate" title="VolterraCertificate">VolterraCertificate</a>" : <i>Boolean</i>,
    "<a href="#volterratrustedca" title="VolterraTrustedCa">VolterraTrustedCa</a>" : <i>Boolean</i>,
    "<a href="#customcertificate" title="CustomCertificate">CustomCertificate</a>" : <i>[ <a href="customcertificatedefinition.md">CustomCertificateDefinition</a>, ... ]</i>,
    "<a href="#policy" title="Policy">Policy</a>" : <i>[ <a href="policydefinition.md">PolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enableforalldomains" title="EnableForAllDomains">EnableForAllDomains</a>: <i>Boolean</i>
<a href="#trustedcaurl" title="TrustedCaUrl">TrustedCaUrl</a>: <i>String</i>
<a href="#volterracertificate" title="VolterraCertificate">VolterraCertificate</a>: <i>Boolean</i>
<a href="#volterratrustedca" title="VolterraTrustedCa">VolterraTrustedCa</a>: <i>Boolean</i>
<a href="#customcertificate" title="CustomCertificate">CustomCertificate</a>: <i>
      - <a href="customcertificatedefinition.md">CustomCertificateDefinition</a></i>
<a href="#policy" title="Policy">Policy</a>: <i>
      - <a href="policydefinition.md">PolicyDefinition</a></i>
</pre>

## Properties

#### EnableForAllDomains

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedCaUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolterraCertificate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolterraTrustedCa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCertificate

_Required_: No

_Type_: List of <a href="customcertificatedefinition.md">CustomCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: List of <a href="policydefinition.md">PolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

