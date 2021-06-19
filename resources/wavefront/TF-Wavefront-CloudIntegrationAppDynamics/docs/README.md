# TF::Wavefront::CloudIntegrationAppDynamics

CloudFormation equivalent of wavefront_cloud_integration_app_dynamics

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Wavefront::CloudIntegrationAppDynamics",
    "Properties" : {
        "<a href="#additionaltags" title="AdditionalTags">AdditionalTags</a>" : <i>[ <a href="additionaltagsdefinition.md">AdditionalTagsDefinition</a>, ... ]</i>,
        "<a href="#appfilterregex" title="AppFilterRegex">AppFilterRegex</a>" : <i>[ String, ... ]</i>,
        "<a href="#controllername" title="ControllerName">ControllerName</a>" : <i>String</i>,
        "<a href="#enableappinframetrics" title="EnableAppInfraMetrics">EnableAppInfraMetrics</a>" : <i>Boolean</i>,
        "<a href="#enablebackendmetrics" title="EnableBackendMetrics">EnableBackendMetrics</a>" : <i>Boolean</i>,
        "<a href="#enablebusinesstrxmetrics" title="EnableBusinessTrxMetrics">EnableBusinessTrxMetrics</a>" : <i>Boolean</i>,
        "<a href="#enableerrormetrics" title="EnableErrorMetrics">EnableErrorMetrics</a>" : <i>Boolean</i>,
        "<a href="#enableindividualnodemetrics" title="EnableIndividualNodeMetrics">EnableIndividualNodeMetrics</a>" : <i>Boolean</i>,
        "<a href="#enableoverallperfmetrics" title="EnableOverallPerfMetrics">EnableOverallPerfMetrics</a>" : <i>Boolean</i>,
        "<a href="#enablerollup" title="EnableRollup">EnableRollup</a>" : <i>Boolean</i>,
        "<a href="#enableserviceendpointmetrics" title="EnableServiceEndpointMetrics">EnableServiceEndpointMetrics</a>" : <i>Boolean</i>,
        "<a href="#encryptedpassword" title="EncryptedPassword">EncryptedPassword</a>" : <i>String</i>,
        "<a href="#forcesave" title="ForceSave">ForceSave</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#servicerefreshrateinminutes" title="ServiceRefreshRateInMinutes">ServiceRefreshRateInMinutes</a>" : <i>Double</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Wavefront::CloudIntegrationAppDynamics
Properties:
    <a href="#additionaltags" title="AdditionalTags">AdditionalTags</a>: <i>
      - <a href="additionaltagsdefinition.md">AdditionalTagsDefinition</a></i>
    <a href="#appfilterregex" title="AppFilterRegex">AppFilterRegex</a>: <i>
      - String</i>
    <a href="#controllername" title="ControllerName">ControllerName</a>: <i>String</i>
    <a href="#enableappinframetrics" title="EnableAppInfraMetrics">EnableAppInfraMetrics</a>: <i>Boolean</i>
    <a href="#enablebackendmetrics" title="EnableBackendMetrics">EnableBackendMetrics</a>: <i>Boolean</i>
    <a href="#enablebusinesstrxmetrics" title="EnableBusinessTrxMetrics">EnableBusinessTrxMetrics</a>: <i>Boolean</i>
    <a href="#enableerrormetrics" title="EnableErrorMetrics">EnableErrorMetrics</a>: <i>Boolean</i>
    <a href="#enableindividualnodemetrics" title="EnableIndividualNodeMetrics">EnableIndividualNodeMetrics</a>: <i>Boolean</i>
    <a href="#enableoverallperfmetrics" title="EnableOverallPerfMetrics">EnableOverallPerfMetrics</a>: <i>Boolean</i>
    <a href="#enablerollup" title="EnableRollup">EnableRollup</a>: <i>Boolean</i>
    <a href="#enableserviceendpointmetrics" title="EnableServiceEndpointMetrics">EnableServiceEndpointMetrics</a>: <i>Boolean</i>
    <a href="#encryptedpassword" title="EncryptedPassword">EncryptedPassword</a>: <i>String</i>
    <a href="#forcesave" title="ForceSave">ForceSave</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#servicerefreshrateinminutes" title="ServiceRefreshRateInMinutes">ServiceRefreshRateInMinutes</a>: <i>Double</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
</pre>

## Properties

#### AdditionalTags

_Required_: No

_Type_: List of <a href="additionaltagsdefinition.md">AdditionalTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppFilterRegex

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAppInfraMetrics

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBackendMetrics

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBusinessTrxMetrics

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableErrorMetrics

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIndividualNodeMetrics

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableOverallPerfMetrics

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRollup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableServiceEndpointMetrics

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptedPassword

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceSave

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRefreshRateInMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

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

#### Id

Returns the <code>Id</code> value.

