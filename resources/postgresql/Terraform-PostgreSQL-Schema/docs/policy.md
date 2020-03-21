# Terraform::PostgreSQL::Schema Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#create" title="Create">Create</a>" : <i>Boolean</i>,
    "<a href="#createwithgrant" title="CreateWithGrant">CreateWithGrant</a>" : <i>Boolean</i>,
    "<a href="#role" title="Role">Role</a>" : <i>String</i>,
    "<a href="#usage" title="Usage">Usage</a>" : <i>Boolean</i>,
    "<a href="#usagewithgrant" title="UsageWithGrant">UsageWithGrant</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#create" title="Create">Create</a>: <i>Boolean</i>
<a href="#createwithgrant" title="CreateWithGrant">CreateWithGrant</a>: <i>Boolean</i>
<a href="#role" title="Role">Role</a>: <i>String</i>
<a href="#usage" title="Usage">Usage</a>: <i>Boolean</i>
<a href="#usagewithgrant" title="UsageWithGrant">UsageWithGrant</a>: <i>Boolean</i>
</pre>

## Properties

#### Create

Should the specified ROLE have CREATE privileges to the specified SCHEMA.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateWithGrant

Should the specified ROLE have CREATE privileges to the specified SCHEMA and the ability to GRANT the CREATE privilege to other ROLEs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The ROLE who is receiving the policy.  If this value is empty or not specified it implies the policy is referring to the [`PUBLIC` role](https://www.postgresql.org/docs/current/static/sql-grant.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usage

Should the specified ROLE have USAGE privileges to the specified SCHEMA.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsageWithGrant

Should the specified ROLE have USAGE privileges to the specified SCHEMA and the ability to GRANT the USAGE privilege to other ROLEs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

