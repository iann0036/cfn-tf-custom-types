# Terraform::Vault::AwsAuthBackendRoleTag

Reads role tag information from an AWS auth backend in Vault.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::AwsAuthBackendRoleTag",
    "Properties" : {
        "<a href="#allowinstancemigration" title="AllowInstanceMigration">AllowInstanceMigration</a>" : <i>Boolean</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#disallowreauthentication" title="DisallowReauthentication">DisallowReauthentication</a>" : <i>Boolean</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>String</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::AwsAuthBackendRoleTag
Properties:
    <a href="#allowinstancemigration" title="AllowInstanceMigration">AllowInstanceMigration</a>: <i>Boolean</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#disallowreauthentication" title="DisallowReauthentication">DisallowReauthentication</a>: <i>Boolean</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
</pre>

## Properties

#### AllowInstanceMigration

If set, allows migration of the underlying instances where the client resides. Use with caution.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

The path to the AWS auth backend to
read role tags from, with no leading or trailing `/`s. Defaults to "aws".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisallowReauthentication

If set, only allows a single token to be granted per instance ID.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

Instance ID for which this tag is intended for. If set, the created tag can only be used by the instance with the given ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

The maximum TTL of the tokens issued using this role.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

The policies to be associated with the tag. Must be a subset of the policies associated with the role.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The name of the AWS auth backend role to read
role tags from, with no leading or trailing `/`s.

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

#### TagKey

Returns the <code>TagKey</code> value.

#### TagValue

Returns the <code>TagValue</code> value.

