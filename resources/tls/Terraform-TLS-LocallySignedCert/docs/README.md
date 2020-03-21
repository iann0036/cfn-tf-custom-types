# Terraform::TLS::LocallySignedCert

CloudFormation equivalent of tls_locally_signed_cert

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TLS::LocallySignedCert",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#alloweduses" title="AllowedUses">AllowedUses</a>" : <i>[ String, ... ]</i>,
        "<a href="#cacertpem" title="CaCertPem">CaCertPem</a>" : <i>String</i>,
        "<a href="#cakeyalgorithm" title="CaKeyAlgorithm">CaKeyAlgorithm</a>" : <i>String</i>,
        "<a href="#caprivatekeypem" title="CaPrivateKeyPem">CaPrivateKeyPem</a>" : <i>String</i>,
        "<a href="#certpem" title="CertPem">CertPem</a>" : <i>String</i>,
        "<a href="#certrequestpem" title="CertRequestPem">CertRequestPem</a>" : <i>String</i>,
        "<a href="#earlyrenewalhours" title="EarlyRenewalHours">EarlyRenewalHours</a>" : <i>Double</i>,
        "<a href="#iscacertificate" title="IsCaCertificate">IsCaCertificate</a>" : <i>Boolean</i>,
        "<a href="#readyforrenewal" title="ReadyForRenewal">ReadyForRenewal</a>" : <i>Boolean</i>,
        "<a href="#setsubjectkeyid" title="SetSubjectKeyId">SetSubjectKeyId</a>" : <i>Boolean</i>,
        "<a href="#validityendtime" title="ValidityEndTime">ValidityEndTime</a>" : <i>String</i>,
        "<a href="#validityperiodhours" title="ValidityPeriodHours">ValidityPeriodHours</a>" : <i>Double</i>,
        "<a href="#validitystarttime" title="ValidityStartTime">ValidityStartTime</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TLS::LocallySignedCert
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#alloweduses" title="AllowedUses">AllowedUses</a>: <i>
      - String</i>
    <a href="#cacertpem" title="CaCertPem">CaCertPem</a>: <i>String</i>
    <a href="#cakeyalgorithm" title="CaKeyAlgorithm">CaKeyAlgorithm</a>: <i>String</i>
    <a href="#caprivatekeypem" title="CaPrivateKeyPem">CaPrivateKeyPem</a>: <i>String</i>
    <a href="#certpem" title="CertPem">CertPem</a>: <i>String</i>
    <a href="#certrequestpem" title="CertRequestPem">CertRequestPem</a>: <i>String</i>
    <a href="#earlyrenewalhours" title="EarlyRenewalHours">EarlyRenewalHours</a>: <i>Double</i>
    <a href="#iscacertificate" title="IsCaCertificate">IsCaCertificate</a>: <i>Boolean</i>
    <a href="#readyforrenewal" title="ReadyForRenewal">ReadyForRenewal</a>: <i>Boolean</i>
    <a href="#setsubjectkeyid" title="SetSubjectKeyId">SetSubjectKeyId</a>: <i>Boolean</i>
    <a href="#validityendtime" title="ValidityEndTime">ValidityEndTime</a>: <i>String</i>
    <a href="#validityperiodhours" title="ValidityPeriodHours">ValidityPeriodHours</a>: <i>Double</i>
    <a href="#validitystarttime" title="ValidityStartTime">ValidityStartTime</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUses

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCertPem

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaKeyAlgorithm

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaPrivateKeyPem

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertPem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertRequestPem

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EarlyRenewalHours

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCaCertificate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadyForRenewal

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetSubjectKeyId

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidityEndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidityPeriodHours

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidityStartTime

_Required_: No

_Type_: String

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

