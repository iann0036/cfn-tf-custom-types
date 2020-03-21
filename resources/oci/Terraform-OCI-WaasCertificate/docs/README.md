# Terraform::OCI::WaasCertificate

CloudFormation equivalent of oci_waas_certificate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::WaasCertificate",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#certificatedata" title="CertificateData">CertificateData</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#extensions" title="Extensions">Extensions</a>" : <i>[ &lt;a href=&#34;extensions.md&#34;&gt;Extensions&lt;/a&gt;, ... ]</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;, ... ]</i>,
        "<a href="#istrustverificationdisabled" title="IsTrustVerificationDisabled">IsTrustVerificationDisabled</a>" : <i>Boolean</i>,
        "<a href="#issuedby" title="IssuedBy">IssuedBy</a>" : <i>String</i>,
        "<a href="#issuername" title="IssuerName">IssuerName</a>" : <i>[ &lt;a href=&#34;issuername.md&#34;&gt;IssuerName&lt;/a&gt;, ... ]</i>,
        "<a href="#privatekeydata" title="PrivateKeyData">PrivateKeyData</a>" : <i>String</i>,
        "<a href="#publickeyinfo" title="PublicKeyInfo">PublicKeyInfo</a>" : <i>[ &lt;a href=&#34;publickeyinfo.md&#34;&gt;PublicKeyInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
        "<a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#subjectname" title="SubjectName">SubjectName</a>" : <i>[ &lt;a href=&#34;subjectname.md&#34;&gt;SubjectName&lt;/a&gt;, ... ]</i>,
        "<a href="#timecreated" title="TimeCreated">TimeCreated</a>" : <i>String</i>,
        "<a href="#timenotvalidafter" title="TimeNotValidAfter">TimeNotValidAfter</a>" : <i>String</i>,
        "<a href="#timenotvalidbefore" title="TimeNotValidBefore">TimeNotValidBefore</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::WaasCertificate
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#certificatedata" title="CertificateData">CertificateData</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#extensions" title="Extensions">Extensions</a>: <i>
      - &lt;a href=&#34;extensions.md&#34;&gt;Extensions&lt;/a&gt;</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;</i>
    <a href="#istrustverificationdisabled" title="IsTrustVerificationDisabled">IsTrustVerificationDisabled</a>: <i>Boolean</i>
    <a href="#issuedby" title="IssuedBy">IssuedBy</a>: <i>String</i>
    <a href="#issuername" title="IssuerName">IssuerName</a>: <i>
      - &lt;a href=&#34;issuername.md&#34;&gt;IssuerName&lt;/a&gt;</i>
    <a href="#privatekeydata" title="PrivateKeyData">PrivateKeyData</a>: <i>String</i>
    <a href="#publickeyinfo" title="PublicKeyInfo">PublicKeyInfo</a>: <i>
      - &lt;a href=&#34;publickeyinfo.md&#34;&gt;PublicKeyInfo&lt;/a&gt;</i>
    <a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
    <a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#subjectname" title="SubjectName">SubjectName</a>: <i>
      - &lt;a href=&#34;subjectname.md&#34;&gt;SubjectName&lt;/a&gt;</i>
    <a href="#timecreated" title="TimeCreated">TimeCreated</a>: <i>String</i>
    <a href="#timenotvalidafter" title="TimeNotValidAfter">TimeNotValidAfter</a>: <i>String</i>
    <a href="#timenotvalidbefore" title="TimeNotValidBefore">TimeNotValidBefore</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateData

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extensions

_Required_: No

_Type_: List of &lt;a href=&#34;extensions.md&#34;&gt;Extensions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsTrustVerificationDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuedBy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerName

_Required_: No

_Type_: List of &lt;a href=&#34;issuername.md&#34;&gt;IssuerName&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyData

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeyInfo

_Required_: No

_Type_: List of &lt;a href=&#34;publickeyinfo.md&#34;&gt;PublicKeyInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignatureAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectName

_Required_: No

_Type_: List of &lt;a href=&#34;subjectname.md&#34;&gt;SubjectName&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeCreated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeNotValidAfter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeNotValidBefore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Extensions

Returns the &lt;code&gt;Extensions&lt;/code&gt; value.

#### IssuedBy

Returns the &lt;code&gt;IssuedBy&lt;/code&gt; value.

#### IssuerName

Returns the &lt;code&gt;IssuerName&lt;/code&gt; value.

#### PublicKeyInfo

Returns the &lt;code&gt;PublicKeyInfo&lt;/code&gt; value.

#### SerialNumber

Returns the &lt;code&gt;SerialNumber&lt;/code&gt; value.

#### SignatureAlgorithm

Returns the &lt;code&gt;SignatureAlgorithm&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### SubjectName

Returns the &lt;code&gt;SubjectName&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.

#### TimeNotValidAfter

Returns the &lt;code&gt;TimeNotValidAfter&lt;/code&gt; value.

#### TimeNotValidBefore

Returns the &lt;code&gt;TimeNotValidBefore&lt;/code&gt; value.

#### Version

Returns the &lt;code&gt;Version&lt;/code&gt; value.

