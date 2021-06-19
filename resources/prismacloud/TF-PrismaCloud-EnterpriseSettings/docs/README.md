# TF::PrismaCloud::EnterpriseSettings

Manages enterprise settings config.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PrismaCloud::EnterpriseSettings",
    "Properties" : {
        "<a href="#anomalyalertdisposition" title="AnomalyAlertDisposition">AnomalyAlertDisposition</a>" : <i>String</i>,
        "<a href="#anomalytrainingmodelthreshold" title="AnomalyTrainingModelThreshold">AnomalyTrainingModelThreshold</a>" : <i>String</i>,
        "<a href="#applydefaultpoliciesenabled" title="ApplyDefaultPoliciesEnabled">ApplyDefaultPoliciesEnabled</a>" : <i>Boolean</i>,
        "<a href="#defaultpoliciesenabled" title="DefaultPoliciesEnabled">DefaultPoliciesEnabled</a>" : <i>[ <a href="defaultpoliciesenableddefinition.md">DefaultPoliciesEnabledDefinition</a>, ... ]</i>,
        "<a href="#requirealertdismissalnote" title="RequireAlertDismissalNote">RequireAlertDismissalNote</a>" : <i>Boolean</i>,
        "<a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>" : <i>Double</i>,
        "<a href="#userattributioninnotification" title="UserAttributionInNotification">UserAttributionInNotification</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PrismaCloud::EnterpriseSettings
Properties:
    <a href="#anomalyalertdisposition" title="AnomalyAlertDisposition">AnomalyAlertDisposition</a>: <i>String</i>
    <a href="#anomalytrainingmodelthreshold" title="AnomalyTrainingModelThreshold">AnomalyTrainingModelThreshold</a>: <i>String</i>
    <a href="#applydefaultpoliciesenabled" title="ApplyDefaultPoliciesEnabled">ApplyDefaultPoliciesEnabled</a>: <i>Boolean</i>
    <a href="#defaultpoliciesenabled" title="DefaultPoliciesEnabled">DefaultPoliciesEnabled</a>: <i>
      - <a href="defaultpoliciesenableddefinition.md">DefaultPoliciesEnabledDefinition</a></i>
    <a href="#requirealertdismissalnote" title="RequireAlertDismissalNote">RequireAlertDismissalNote</a>: <i>Boolean</i>
    <a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>: <i>Double</i>
    <a href="#userattributioninnotification" title="UserAttributionInNotification">UserAttributionInNotification</a>: <i>Boolean</i>
</pre>

## Properties

#### AnomalyAlertDisposition

Anomaly alert disposition (`low`, `medium`, or `high`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnomalyTrainingModelThreshold

Anomaly training model threshold (`low`, `medium`, or `high`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyDefaultPoliciesEnabled

Apply default policies enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPoliciesEnabled

Default policies enabled.

_Required_: No

_Type_: List of <a href="defaultpoliciesenableddefinition.md">DefaultPoliciesEnabledDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireAlertDismissalNote

Require alert dismissal note.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTimeout

Browser session timeout.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAttributionInNotification

User attribution in notification.

_Required_: No

_Type_: Boolean

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

