# TF::Aviatrix::AwsTgwSecurityDomain

The **aviatrix_aws_tgw_security_domain** resource allows the creation and management of Aviatrix security domains.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::AwsTgwSecurityDomain",
    "Properties" : {
        "<a href="#aviatrixfirewall" title="AviatrixFirewall">AviatrixFirewall</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nativeegress" title="NativeEgress">NativeEgress</a>" : <i>Boolean</i>,
        "<a href="#nativefirewall" title="NativeFirewall">NativeFirewall</a>" : <i>Boolean</i>,
        "<a href="#tgwname" title="TgwName">TgwName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::AwsTgwSecurityDomain
Properties:
    <a href="#aviatrixfirewall" title="AviatrixFirewall">AviatrixFirewall</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nativeegress" title="NativeEgress">NativeEgress</a>: <i>Boolean</i>
    <a href="#nativefirewall" title="NativeFirewall">NativeFirewall</a>: <i>Boolean</i>
    <a href="#tgwname" title="TgwName">TgwName</a>: <i>String</i>
</pre>

## Properties

#### AviatrixFirewall

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NativeEgress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NativeFirewall

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwName

_Required_: Yes

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

