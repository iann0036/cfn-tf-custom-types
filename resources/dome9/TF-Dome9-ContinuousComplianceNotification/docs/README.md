# TF::Dome9::ContinuousComplianceNotification

This resource is used  to create and modify Dome9  notification policies for Continuous Compliance assessments of cloud accounts. Continuous assessments apply bundles of compliance rules to your cloud account continuously, and send notifications of issues according to the Notification Policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::ContinuousComplianceNotification",
    "Properties" : {
        "<a href="#alertsconsole" title="AlertsConsole">AlertsConsole</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#changedetection" title="ChangeDetection">ChangeDetection</a>" : <i>[ <a href="changedetectiondefinition.md">ChangeDetectionDefinition</a>, ... ]</i>,
        "<a href="#gcpsecuritycommandcenterintegration" title="GcpSecurityCommandCenterIntegration">GcpSecurityCommandCenterIntegration</a>" : <i>[ <a href="gcpsecuritycommandcenterintegrationdefinition.md">GcpSecurityCommandCenterIntegrationDefinition</a>, ... ]</i>,
        "<a href="#scheduledreport" title="ScheduledReport">ScheduledReport</a>" : <i>[ <a href="scheduledreportdefinition.md">ScheduledReportDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::ContinuousComplianceNotification
Properties:
    <a href="#alertsconsole" title="AlertsConsole">AlertsConsole</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#changedetection" title="ChangeDetection">ChangeDetection</a>: <i>
      - <a href="changedetectiondefinition.md">ChangeDetectionDefinition</a></i>
    <a href="#gcpsecuritycommandcenterintegration" title="GcpSecurityCommandCenterIntegration">GcpSecurityCommandCenterIntegration</a>: <i>
      - <a href="gcpsecuritycommandcenterintegrationdefinition.md">GcpSecurityCommandCenterIntegrationDefinition</a></i>
    <a href="#scheduledreport" title="ScheduledReport">ScheduledReport</a>: <i>
      - <a href="scheduledreportdefinition.md">ScheduledReportDefinition</a></i>
</pre>

## Properties

#### AlertsConsole

send  findings (also) to the Dome9 web app alerts console (Boolean); default is False.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the notification.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The cloud account id in Dome9.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeDetection

_Required_: No

_Type_: List of <a href="changedetectiondefinition.md">ChangeDetectionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpSecurityCommandCenterIntegration

_Required_: No

_Type_: List of <a href="gcpsecuritycommandcenterintegrationdefinition.md">GcpSecurityCommandCenterIntegrationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledReport

_Required_: No

_Type_: List of <a href="scheduledreportdefinition.md">ScheduledReportDefinition</a>

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

