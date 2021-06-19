# TF::Cloudflare::AccessGroup

Provides a Cloudflare Access Group resource. Access Groups are used
in conjunction with Access Policies to restrict access to a
particular resource based on group membership.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::AccessGroup",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#exclude" title="Exclude">Exclude</a>" : <i>[ <a href="excludedefinition.md">ExcludeDefinition</a>, ... ]</i>,
        "<a href="#include" title="Include">Include</a>" : <i>[ <a href="includedefinition.md">IncludeDefinition</a>, ... ]</i>,
        "<a href="#require" title="Require">Require</a>" : <i>[ <a href="requiredefinition.md">RequireDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::AccessGroup
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#exclude" title="Exclude">Exclude</a>: <i>
      - <a href="excludedefinition.md">ExcludeDefinition</a></i>
    <a href="#include" title="Include">Include</a>: <i>
      - <a href="includedefinition.md">IncludeDefinition</a></i>
    <a href="#require" title="Require">Require</a>: <i>
      - <a href="requiredefinition.md">RequireDefinition</a></i>
</pre>

## Properties

#### AccountId

The ID of the account the group is associated with. Conflicts with `zone_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Friendly name of the Access Group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The ID of the zone the group is associated with. Conflicts with `account_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclude

_Required_: No

_Type_: List of <a href="excludedefinition.md">ExcludeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Include

_Required_: No

_Type_: List of <a href="includedefinition.md">IncludeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Require

_Required_: No

_Type_: List of <a href="requiredefinition.md">RequireDefinition</a>

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

