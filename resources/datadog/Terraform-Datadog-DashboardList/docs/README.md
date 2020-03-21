# Terraform::Datadog::DashboardList

Provides a Datadog dashboard_list resource. This can be used to create and manage Datadog Dashboard Lists and the individual dashboards within them.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::DashboardList",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#dashitem" title="DashItem">DashItem</a>" : <i>[ <a href="dashitem.md">DashItem</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::DashboardList
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#dashitem" title="DashItem">DashItem</a>: <i>
      - <a href="dashitem.md">DashItem</a></i>
</pre>

## Properties

#### Name

The name of this Dashbaord List.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DashItem

_Required_: No

_Type_: List of <a href="dashitem.md">DashItem</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

