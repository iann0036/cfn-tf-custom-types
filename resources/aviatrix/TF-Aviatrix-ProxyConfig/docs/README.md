# TF::Aviatrix::ProxyConfig

The **aviatrix_proxy_config** resource allows management of an Aviatrix Controller's proxy configurations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::ProxyConfig",
    "Properties" : {
        "<a href="#httpproxy" title="HttpProxy">HttpProxy</a>" : <i>String</i>,
        "<a href="#httpsproxy" title="HttpsProxy">HttpsProxy</a>" : <i>String</i>,
        "<a href="#proxycacertificate" title="ProxyCaCertificate">ProxyCaCertificate</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::ProxyConfig
Properties:
    <a href="#httpproxy" title="HttpProxy">HttpProxy</a>: <i>String</i>
    <a href="#httpsproxy" title="HttpsProxy">HttpsProxy</a>: <i>String</i>
    <a href="#proxycacertificate" title="ProxyCaCertificate">ProxyCaCertificate</a>: <i>String</i>
</pre>

## Properties

#### HttpProxy

Http proxy URL.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsProxy

Https proxy URL.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyCaCertificate

Server CA Certificate file. Use the `file` function to read from a file.

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

#### Id

Returns the <code>Id</code> value.

