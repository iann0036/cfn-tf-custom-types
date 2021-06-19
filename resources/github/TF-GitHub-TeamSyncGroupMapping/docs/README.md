# TF::GitHub::TeamSyncGroupMapping

This resource allows you to create and manage Identity Provider (IdP) group connections within your GitHub teams.
You must have team synchronization enabled for organizations owned by enterprise accounts.

To learn more about team synchronization between IdPs and Github, please refer to:
https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/synchronizing-teams-between-your-identity-provider-and-github

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::TeamSyncGroupMapping",
    "Properties" : {
        "<a href="#teamslug" title="TeamSlug">TeamSlug</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>[ <a href="groupdefinition.md">GroupDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::TeamSyncGroupMapping
Properties:
    <a href="#teamslug" title="TeamSlug">TeamSlug</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>
      - <a href="groupdefinition.md">GroupDefinition</a></i>
</pre>

## Properties

#### TeamSlug

Slug of the team.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: List of <a href="groupdefinition.md">GroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Etag

Returns the <code>Etag</code> value.

#### Id

Returns the <code>Id</code> value.

