# Terraform::ACME::Certificate

CloudFormation equivalent of acme_certificate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::ACME::Certificate",
    "Properties" : {
        "<a href="#accountkeypem" title="AccountKeyPem">AccountKeyPem</a>" : <i>String</i>,
        "<a href="#certificatep12password" title="CertificateP12Password">CertificateP12Password</a>" : <i>String</i>,
        "<a href="#certificaterequestpem" title="CertificateRequestPem">CertificateRequestPem</a>" : <i>String</i>,
        "<a href="#commonname" title="CommonName">CommonName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
        "<a href="#mindaysremaining" title="MinDaysRemaining">MinDaysRemaining</a>" : <i>Double</i>,
        "<a href="#muststaple" title="MustStaple">MustStaple</a>" : <i>Boolean</i>,
        "<a href="#recursivenameservers" title="RecursiveNameservers">RecursiveNameservers</a>" : <i>[ String, ... ]</i>,
        "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#dnschallenge" title="DnsChallenge">DnsChallenge</a>" : <i>[ &lt;a href=&#34;dnschallenge.md&#34;&gt;DnsChallenge&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::ACME::Certificate
Properties:
    <a href="#accountkeypem" title="AccountKeyPem">AccountKeyPem</a>: <i>String</i>
    <a href="#certificatep12password" title="CertificateP12Password">CertificateP12Password</a>: <i>String</i>
    <a href="#certificaterequestpem" title="CertificateRequestPem">CertificateRequestPem</a>: <i>String</i>
    <a href="#commonname" title="CommonName">CommonName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
    <a href="#mindaysremaining" title="MinDaysRemaining">MinDaysRemaining</a>: <i>Double</i>
    <a href="#muststaple" title="MustStaple">MustStaple</a>: <i>Boolean</i>
    <a href="#recursivenameservers" title="RecursiveNameservers">RecursiveNameservers</a>: <i>
      - String</i>
    <a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>: <i>
      - String</i>
    <a href="#dnschallenge" title="DnsChallenge">DnsChallenge</a>: <i>
      - &lt;a href=&#34;dnschallenge.md&#34;&gt;DnsChallenge&lt;/a&gt;</i>
</pre>

## Properties

#### AccountKeyPem

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateP12Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateRequestPem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinDaysRemaining

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustStaple

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecursiveNameservers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAlternativeNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsChallenge

_Required_: No

_Type_: List of &lt;a href=&#34;dnschallenge.md&#34;&gt;DnsChallenge&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CertificateDomain

Returns the &lt;code&gt;CertificateDomain&lt;/code&gt; value.

#### CertificateP12

Returns the &lt;code&gt;CertificateP12&lt;/code&gt; value.

#### CertificatePem

Returns the &lt;code&gt;CertificatePem&lt;/code&gt; value.

#### CertificateUrl

Returns the &lt;code&gt;CertificateUrl&lt;/code&gt; value.

#### IssuerPem

Returns the &lt;code&gt;IssuerPem&lt;/code&gt; value.

#### PrivateKeyPem

Returns the &lt;code&gt;PrivateKeyPem&lt;/code&gt; value.

