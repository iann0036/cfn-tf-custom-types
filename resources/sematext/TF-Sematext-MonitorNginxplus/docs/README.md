# TF::Sematext::MonitorNginxplus

CloudFormation equivalent of sematext_monitor_nginxplus

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Sematext::MonitorNginxplus",
    "Properties" : {
        "<a href="#billingplanid" title="BillingPlanId">BillingPlanId</a>" : <i>Double</i>,
        "<a href="#discountcode" title="DiscountCode">DiscountCode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#apptoken" title="Apptoken">Apptoken</a>" : <i>[ <a href="apptokendefinition.md">ApptokenDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Sematext::MonitorNginxplus
Properties:
    <a href="#billingplanid" title="BillingPlanId">BillingPlanId</a>: <i>Double</i>
    <a href="#discountcode" title="DiscountCode">DiscountCode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#apptoken" title="Apptoken">Apptoken</a>: <i>
      - <a href="apptokendefinition.md">ApptokenDefinition</a></i>
</pre>

## Properties

#### BillingPlanId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscountCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Apptoken

_Required_: No

_Type_: List of <a href="apptokendefinition.md">ApptokenDefinition</a>

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

#### ScApptokenEntries

Returns the <code>ScApptokenEntries</code> value.

