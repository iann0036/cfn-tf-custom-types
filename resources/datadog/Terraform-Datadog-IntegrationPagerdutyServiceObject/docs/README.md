# Terraform::Datadog::IntegrationPagerdutyServiceObject

Provides access to individual Service Objects of Datadog - PagerDuty integrations. Note that the Datadog - PagerDuty integration must be activated (either manually in the Datadog UI or by using [datadog_integration_pagerduty](/docs/providers/datadog/r/integration_pagerduty.html)) in order for this resource to be usable.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::IntegrationPagerdutyServiceObject",
    "Properties" : {
        "<a href="#servicekey" title="ServiceKey">ServiceKey</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::IntegrationPagerdutyServiceObject
Properties:
    <a href="#servicekey" title="ServiceKey">ServiceKey</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
</pre>

## Properties

#### ServiceKey

Your Service name associated service key in PagerDuty. Note: Since the Datadog API never returns service keys, it is impossible to detect [drifts](https://www.hashicorp.com/blog/detecting-and-managing-drift-with-terraform). The best way to solve a drift is to manually mark the Service Object resource with [terraform taint](https://www.terraform.io/docs/commands/taint.html) to have it destroyed and recreated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

Your Service name in PagerDuty.

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

