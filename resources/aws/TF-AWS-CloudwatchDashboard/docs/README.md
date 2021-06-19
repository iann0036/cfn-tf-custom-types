# TF::AWS::CloudwatchDashboard

Provides a CloudWatch Dashboard resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudwatchDashboard",
    "Properties" : {
        "<a href="#dashboardbody" title="DashboardBody">DashboardBody</a>" : <i>String</i>,
        "<a href="#dashboardname" title="DashboardName">DashboardName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudwatchDashboard
Properties:
    <a href="#dashboardbody" title="DashboardBody">DashboardBody</a>: <i>String</i>
    <a href="#dashboardname" title="DashboardName">DashboardName</a>: <i>String</i>
</pre>

## Properties

#### DashboardBody

The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DashboardName

The name of the dashboard.

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

#### DashboardArn

Returns the <code>DashboardArn</code> value.

#### Id

Returns the <code>Id</code> value.

