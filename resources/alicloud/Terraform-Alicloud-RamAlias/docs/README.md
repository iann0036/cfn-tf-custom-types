# Terraform::Alicloud::RamAlias

-> **NOTE:** This resource has been deprecated from [v1.3.2](https://github.com/alibaba/terraform-provider/releases/tag/V1.3.2). New resource `alicloud_ram_account_alias` will replace.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::RamAlias",
    "Properties" : {
        "<a href="#accountalias" title="AccountAlias">AccountAlias</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::RamAlias
Properties:
    <a href="#accountalias" title="AccountAlias">AccountAlias</a>: <i>String</i>
</pre>

## Properties

#### AccountAlias

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

