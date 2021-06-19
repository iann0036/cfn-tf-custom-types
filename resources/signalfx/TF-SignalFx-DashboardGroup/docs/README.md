# TF::SignalFx::DashboardGroup

In the SignalFx web UI, a [dashboard group](https://developers.signalfx.com/dashboard_groups_reference.html) is a collection of dashboards.

~> **NOTE** Dashboard groups cannot be accessed directly, but just via a dashboard contained in them. This is the reason why make show won't show any of yours dashboard groups.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::DashboardGroup",
    "Properties" : {
        "<a href="#authorizedwriterteams" title="AuthorizedWriterTeams">AuthorizedWriterTeams</a>" : <i>[ String, ... ]</i>,
        "<a href="#authorizedwriterusers" title="AuthorizedWriterUsers">AuthorizedWriterUsers</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#teams" title="Teams">Teams</a>" : <i>[ String, ... ]</i>,
        "<a href="#dashboard" title="Dashboard">Dashboard</a>" : <i>[ <a href="dashboarddefinition.md">DashboardDefinition</a>, ... ]</i>,
        "<a href="#importqualifier" title="ImportQualifier">ImportQualifier</a>" : <i>[ <a href="importqualifierdefinition.md">ImportQualifierDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::DashboardGroup
Properties:
    <a href="#authorizedwriterteams" title="AuthorizedWriterTeams">AuthorizedWriterTeams</a>: <i>
      - String</i>
    <a href="#authorizedwriterusers" title="AuthorizedWriterUsers">AuthorizedWriterUsers</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#teams" title="Teams">Teams</a>: <i>
      - String</i>
    <a href="#dashboard" title="Dashboard">Dashboard</a>: <i>
      - <a href="dashboarddefinition.md">DashboardDefinition</a></i>
    <a href="#importqualifier" title="ImportQualifier">ImportQualifier</a>: <i>
      - <a href="importqualifierdefinition.md">ImportQualifierDefinition</a></i>
</pre>

## Properties

#### AuthorizedWriterTeams

Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedWriterUsers

User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the dashboard group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the dashboard group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teams

Team IDs to associate the dashboard group to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dashboard

_Required_: No

_Type_: List of <a href="dashboarddefinition.md">DashboardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportQualifier

_Required_: No

_Type_: List of <a href="importqualifierdefinition.md">ImportQualifierDefinition</a>

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

