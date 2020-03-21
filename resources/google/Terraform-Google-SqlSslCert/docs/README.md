# Terraform::Google::SqlSslCert

CloudFormation equivalent of google_sql_ssl_cert

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::SqlSslCert",
    "Properties" : {
        "<a href="#commonname" title="CommonName">CommonName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#instance" title="Instance">Instance</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::SqlSslCert
Properties:
    <a href="#commonname" title="CommonName">CommonName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#instance" title="Instance">Instance</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
</pre>

## Properties

#### CommonName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instance

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

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

#### Cert

Returns the &lt;code&gt;Cert&lt;/code&gt; value.

#### CertSerialNumber

Returns the &lt;code&gt;CertSerialNumber&lt;/code&gt; value.

#### CreateTime

Returns the &lt;code&gt;CreateTime&lt;/code&gt; value.

#### ExpirationTime

Returns the &lt;code&gt;ExpirationTime&lt;/code&gt; value.

#### PrivateKey

Returns the &lt;code&gt;PrivateKey&lt;/code&gt; value.

#### ServerCaCert

Returns the &lt;code&gt;ServerCaCert&lt;/code&gt; value.

#### Sha1Fingerprint

Returns the &lt;code&gt;Sha1Fingerprint&lt;/code&gt; value.

