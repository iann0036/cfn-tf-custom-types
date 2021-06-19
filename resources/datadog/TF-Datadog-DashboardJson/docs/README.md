# TF::Datadog::DashboardJson

CloudFormation equivalent of datadog_dashboard_json

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Datadog::DashboardJson",
    "Properties" : {
        "<a href="#dashboard" title="Dashboard">Dashboard</a>" : <i>String</i>,
        "<a href="#dashboardlists" title="DashboardLists">DashboardLists</a>" : <i>[ Double, ... ]</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Datadog::DashboardJson
Properties:
    <a href="#dashboard" title="Dashboard">Dashboard</a>: <i>String</i>
    <a href="#dashboardlists" title="DashboardLists">DashboardLists</a>: <i>
      - Double</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### Dashboard

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DashboardLists

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

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

#### DashboardListsRemoved

Returns the <code>DashboardListsRemoved</code> value.

#### Id

Returns the <code>Id</code> value.

