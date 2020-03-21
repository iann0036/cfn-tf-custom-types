# Terraform::Cloudflare::CustomSsl

CloudFormation equivalent of cloudflare_custom_ssl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::CustomSsl",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#customssloptions" title="CustomSslOptions">CustomSslOptions</a>" : <i>[ &lt;a href=&#34;customssloptions.md&#34;&gt;CustomSslOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#expireson" title="ExpiresOn">ExpiresOn</a>" : <i>String</i>,
        "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ String, ... ]</i>,
        "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
        "<a href="#modifiedon" title="ModifiedOn">ModifiedOn</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#signature" title="Signature">Signature</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#uploadedon" title="UploadedOn">UploadedOn</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#customsslpriority" title="CustomSslPriority">CustomSslPriority</a>" : <i>[ &lt;a href=&#34;customsslpriority.md&#34;&gt;CustomSslPriority&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::CustomSsl
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#customssloptions" title="CustomSslOptions">CustomSslOptions</a>: <i>
      - &lt;a href=&#34;customssloptions.md&#34;&gt;CustomSslOptions&lt;/a&gt;</i>
    <a href="#expireson" title="ExpiresOn">ExpiresOn</a>: <i>String</i>
    <a href="#hosts" title="Hosts">Hosts</a>: <i>
      - String</i>
    <a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
    <a href="#modifiedon" title="ModifiedOn">ModifiedOn</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#signature" title="Signature">Signature</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#uploadedon" title="UploadedOn">UploadedOn</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#customsslpriority" title="CustomSslPriority">CustomSslPriority</a>: <i>
      - &lt;a href=&#34;customsslpriority.md&#34;&gt;CustomSslPriority&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSslOptions

_Required_: No

_Type_: List of &lt;a href=&#34;customssloptions.md&#34;&gt;CustomSslOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiresOn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModifiedOn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signature

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadedOn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSslPriority

_Required_: No

_Type_: List of &lt;a href=&#34;customsslpriority.md&#34;&gt;CustomSslPriority&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ExpiresOn

Returns the &lt;code&gt;ExpiresOn&lt;/code&gt; value.

#### Hosts

Returns the &lt;code&gt;Hosts&lt;/code&gt; value.

#### Issuer

Returns the &lt;code&gt;Issuer&lt;/code&gt; value.

#### ModifiedOn

Returns the &lt;code&gt;ModifiedOn&lt;/code&gt; value.

#### Priority

Returns the &lt;code&gt;Priority&lt;/code&gt; value.

#### Signature

Returns the &lt;code&gt;Signature&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### UploadedOn

Returns the &lt;code&gt;UploadedOn&lt;/code&gt; value.

