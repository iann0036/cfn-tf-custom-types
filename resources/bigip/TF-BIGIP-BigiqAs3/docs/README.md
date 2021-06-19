# TF::BIGIP::BigiqAs3

`bigip_bigiq_as3` provides details about bigiq as3 resource

This resource is helpful to configure as3 declarative JSON on BIG-IP through BIG-IQ.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::BigiqAs3",
    "Properties" : {
        "<a href="#as3json" title="As3Json">As3Json</a>" : <i>String</i>,
        "<a href="#bigiqaddress" title="BigiqAddress">BigiqAddress</a>" : <i>String</i>,
        "<a href="#bigiqloginref" title="BigiqLoginRef">BigiqLoginRef</a>" : <i>String</i>,
        "<a href="#bigiqpassword" title="BigiqPassword">BigiqPassword</a>" : <i>String</i>,
        "<a href="#bigiqport" title="BigiqPort">BigiqPort</a>" : <i>String</i>,
        "<a href="#bigiqtokenauth" title="BigiqTokenAuth">BigiqTokenAuth</a>" : <i>Boolean</i>,
        "<a href="#bigiquser" title="BigiqUser">BigiqUser</a>" : <i>String</i>,
        "<a href="#tenantlist" title="TenantList">TenantList</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::BigiqAs3
Properties:
    <a href="#as3json" title="As3Json">As3Json</a>: <i>String</i>
    <a href="#bigiqaddress" title="BigiqAddress">BigiqAddress</a>: <i>String</i>
    <a href="#bigiqloginref" title="BigiqLoginRef">BigiqLoginRef</a>: <i>String</i>
    <a href="#bigiqpassword" title="BigiqPassword">BigiqPassword</a>: <i>String</i>
    <a href="#bigiqport" title="BigiqPort">BigiqPort</a>: <i>String</i>
    <a href="#bigiqtokenauth" title="BigiqTokenAuth">BigiqTokenAuth</a>: <i>Boolean</i>
    <a href="#bigiquser" title="BigiqUser">BigiqUser</a>: <i>String</i>
    <a href="#tenantlist" title="TenantList">TenantList</a>: <i>String</i>
</pre>

## Properties

#### As3Json

Path/Filename of Declarative AS3 JSON which is a json file used with builtin ```file``` function.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqAddress

Address of the BIG-IQ to which your targer BIG-IP is attached.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqLoginRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqPassword

Password of the BIG-IQ to which your targer BIG-IP is attached.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqTokenAuth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqUser

User name  of the BIG-IQ to which your targer BIG-IP is attached.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantList

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

