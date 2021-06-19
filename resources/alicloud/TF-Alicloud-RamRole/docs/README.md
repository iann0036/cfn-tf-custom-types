# TF::Alicloud::RamRole

Provides a RAM Role resource.

-> **NOTE:** When you want to destroy this resource forcefully(means remove all the relationships associated with it automatically and then destroy it) without set `force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::RamRole",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#document" title="Document">Document</a>" : <i>String</i>,
        "<a href="#force" title="Force">Force</a>" : <i>Boolean</i>,
        "<a href="#maxsessionduration" title="MaxSessionDuration">MaxSessionDuration</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ramusers" title="RamUsers">RamUsers</a>" : <i>[ String, ... ]</i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ String, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::RamRole
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#document" title="Document">Document</a>: <i>String</i>
    <a href="#force" title="Force">Force</a>: <i>Boolean</i>
    <a href="#maxsessionduration" title="MaxSessionDuration">MaxSessionDuration</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ramusers" title="RamUsers">RamUsers</a>: <i>
      - String</i>
    <a href="#services" title="Services">Services</a>: <i>
      - String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### Description

Description of the RAM role. This name can have a string of 1 to 1024 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Document

Authorization strategy of the RAM role. It is required when the `services` and `ram_users` are not specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Force

This parameter is used for resource destroy. Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSessionDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the RAM role. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-", "_", and must not begin with a hyphen.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RamUsers

(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of ram users who can assume the RAM role. The format of each item in this list is `acs:ram::${account_id}:root` or `acs:ram::${account_id}:user/${user_name}`, such as `acs:ram::1234567890000:root` and `acs:ram::1234567890001:user/Mary`. The `${user_name}` is the name of a RAM user which must exists in the Alicloud account indicated by the `${account_id}`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of services which can assume the RAM role. The format of each item in this list is `${service}.aliyuncs.com` or `${account_id}@${service}.aliyuncs.com`, such as `ecs.aliyuncs.com` and `1234567890000@ots.aliyuncs.com`. The `${service}` can be `ecs`, `log`, `apigateway` and so on, the `${account_id}` refers to someone's Alicloud account id.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM role policy document. Valid value is `1`. Default value is `1`.

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### RoleId

Returns the <code>RoleId</code> value.

