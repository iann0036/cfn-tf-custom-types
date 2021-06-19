# TF::Thunder::SlbTemplateClientSsh

`thunder_slb_template_client_ssh` Provides details about thunder slb template client ssh

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateClientSsh",
    "Properties" : {
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>String</i>,
        "<a href="#forwardproxyenable" title="ForwardProxyEnable">ForwardProxyEnable</a>" : <i>Double</i>,
        "<a href="#forwardproxyhostkey" title="ForwardProxyHostkey">ForwardProxyHostkey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#passphrase" title="Passphrase">Passphrase</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateClientSsh
Properties:
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>String</i>
    <a href="#forwardproxyenable" title="ForwardProxyEnable">ForwardProxyEnable</a>: <i>Double</i>
    <a href="#forwardproxyhostkey" title="ForwardProxyHostkey">ForwardProxyHostkey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#passphrase" title="Passphrase">Passphrase</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### Encrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyEnable

Enable SSH forward proxy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyHostkey

Specify private-key (Key Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Client SSH Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passphrase

Password Phrase.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

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

