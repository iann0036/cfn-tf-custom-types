# Terraform::TLS::SelfSignedCert

CloudFormation equivalent of tls_self_signed_cert

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TLS::SelfSignedCert",
    "Properties" : {
        "<a href="#alloweduses" title="AllowedUses">AllowedUses</a>" : <i>[ String, ... ]</i>,
        "<a href="#dnsnames" title="DnsNames">DnsNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#earlyrenewalhours" title="EarlyRenewalHours">EarlyRenewalHours</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#iscacertificate" title="IsCaCertificate">IsCaCertificate</a>" : <i>Boolean</i>,
        "<a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>" : <i>String</i>,
        "<a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>" : <i>String</i>,
        "<a href="#setsubjectkeyid" title="SetSubjectKeyId">SetSubjectKeyId</a>" : <i>Boolean</i>,
        "<a href="#uris" title="Uris">Uris</a>" : <i>[ String, ... ]</i>,
        "<a href="#validityperiodhours" title="ValidityPeriodHours">ValidityPeriodHours</a>" : <i>Double</i>,
        "<a href="#subject" title="Subject">Subject</a>" : <i>[ &lt;a href=&#34;subject.md&#34;&gt;Subject&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TLS::SelfSignedCert
Properties:
    <a href="#alloweduses" title="AllowedUses">AllowedUses</a>: <i>
      - String</i>
    <a href="#dnsnames" title="DnsNames">DnsNames</a>: <i>
      - String</i>
    <a href="#earlyrenewalhours" title="EarlyRenewalHours">EarlyRenewalHours</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#ipaddresses" title="IpAddresses">IpAddresses</a>: <i>
      - String</i>
    <a href="#iscacertificate" title="IsCaCertificate">IsCaCertificate</a>: <i>Boolean</i>
    <a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>: <i>String</i>
    <a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>: <i>String</i>
    <a href="#setsubjectkeyid" title="SetSubjectKeyId">SetSubjectKeyId</a>: <i>Boolean</i>
    <a href="#uris" title="Uris">Uris</a>: <i>
      - String</i>
    <a href="#validityperiodhours" title="ValidityPeriodHours">ValidityPeriodHours</a>: <i>Double</i>
    <a href="#subject" title="Subject">Subject</a>: <i>
      - &lt;a href=&#34;subject.md&#34;&gt;Subject&lt;/a&gt;</i>
</pre>

## Properties

#### AllowedUses

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EarlyRenewalHours

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCaCertificate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAlgorithm

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyPem

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetSubjectKeyId

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uris

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidityPeriodHours

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: No

_Type_: List of &lt;a href=&#34;subject.md&#34;&gt;Subject&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CertPem

Returns the &lt;code&gt;CertPem&lt;/code&gt; value.

#### ReadyForRenewal

Returns the &lt;code&gt;ReadyForRenewal&lt;/code&gt; value.

#### ValidityEndTime

Returns the &lt;code&gt;ValidityEndTime&lt;/code&gt; value.

#### ValidityStartTime

Returns the &lt;code&gt;ValidityStartTime&lt;/code&gt; value.

