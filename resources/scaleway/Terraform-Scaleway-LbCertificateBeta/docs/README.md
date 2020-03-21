# Terraform::Scaleway::LbCertificateBeta

CloudFormation equivalent of scaleway_lb_certificate_beta

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::LbCertificateBeta",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#lbid" title="LbId">LbId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#customcertificate" title="CustomCertificate">CustomCertificate</a>" : <i>[ &lt;a href=&#34;customcertificate.md&#34;&gt;CustomCertificate&lt;/a&gt;, ... ]</i>,
        "<a href="#letsencrypt" title="Letsencrypt">Letsencrypt</a>" : <i>[ &lt;a href=&#34;letsencrypt.md&#34;&gt;Letsencrypt&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::LbCertificateBeta
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#lbid" title="LbId">LbId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#customcertificate" title="CustomCertificate">CustomCertificate</a>: <i>
      - &lt;a href=&#34;customcertificate.md&#34;&gt;CustomCertificate&lt;/a&gt;</i>
    <a href="#letsencrypt" title="Letsencrypt">Letsencrypt</a>: <i>
      - &lt;a href=&#34;letsencrypt.md&#34;&gt;Letsencrypt&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;customcertificate.md&#34;&gt;CustomCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Letsencrypt

_Required_: No

_Type_: List of &lt;a href=&#34;letsencrypt.md&#34;&gt;Letsencrypt&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CommonName

Returns the &lt;code&gt;CommonName&lt;/code&gt; value.

#### Fingerprint

Returns the &lt;code&gt;Fingerprint&lt;/code&gt; value.

#### NotValidAfter

Returns the &lt;code&gt;NotValidAfter&lt;/code&gt; value.

#### NotValidBefore

Returns the &lt;code&gt;NotValidBefore&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### SubjectAlternativeName

Returns the &lt;code&gt;SubjectAlternativeName&lt;/code&gt; value.

