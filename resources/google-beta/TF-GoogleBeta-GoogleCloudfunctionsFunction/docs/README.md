# TF::GoogleBeta::GoogleCloudfunctionsFunction

CloudFormation equivalent of google_cloudfunctions_function

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleCloudfunctionsFunction",
    "Properties" : {
        "<a href="#availablememorymb" title="AvailableMemoryMb">AvailableMemoryMb</a>" : <i>Double</i>,
        "<a href="#buildenvironmentvariables" title="BuildEnvironmentVariables">BuildEnvironmentVariables</a>" : <i>[ <a href="buildenvironmentvariablesdefinition.md">BuildEnvironmentVariablesDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#entrypoint" title="EntryPoint">EntryPoint</a>" : <i>String</i>,
        "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>, ... ]</i>,
        "<a href="#httpstriggerurl" title="HttpsTriggerUrl">HttpsTriggerUrl</a>" : <i>String</i>,
        "<a href="#ingresssettings" title="IngressSettings">IngressSettings</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#maxinstances" title="MaxInstances">MaxInstances</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#serviceaccountemail" title="ServiceAccountEmail">ServiceAccountEmail</a>" : <i>String</i>,
        "<a href="#sourcearchivebucket" title="SourceArchiveBucket">SourceArchiveBucket</a>" : <i>String</i>,
        "<a href="#sourcearchiveobject" title="SourceArchiveObject">SourceArchiveObject</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#triggerhttp" title="TriggerHttp">TriggerHttp</a>" : <i>Boolean</i>,
        "<a href="#vpcconnector" title="VpcConnector">VpcConnector</a>" : <i>String</i>,
        "<a href="#vpcconnectoregresssettings" title="VpcConnectorEgressSettings">VpcConnectorEgressSettings</a>" : <i>String</i>,
        "<a href="#eventtrigger" title="EventTrigger">EventTrigger</a>" : <i>[ <a href="eventtriggerdefinition.md">EventTriggerDefinition</a>, ... ]</i>,
        "<a href="#sourcerepository" title="SourceRepository">SourceRepository</a>" : <i>[ <a href="sourcerepositorydefinition.md">SourceRepositoryDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleCloudfunctionsFunction
Properties:
    <a href="#availablememorymb" title="AvailableMemoryMb">AvailableMemoryMb</a>: <i>Double</i>
    <a href="#buildenvironmentvariables" title="BuildEnvironmentVariables">BuildEnvironmentVariables</a>: <i>
      - <a href="buildenvironmentvariablesdefinition.md">BuildEnvironmentVariablesDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#entrypoint" title="EntryPoint">EntryPoint</a>: <i>String</i>
    <a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a></i>
    <a href="#httpstriggerurl" title="HttpsTriggerUrl">HttpsTriggerUrl</a>: <i>String</i>
    <a href="#ingresssettings" title="IngressSettings">IngressSettings</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#maxinstances" title="MaxInstances">MaxInstances</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#serviceaccountemail" title="ServiceAccountEmail">ServiceAccountEmail</a>: <i>String</i>
    <a href="#sourcearchivebucket" title="SourceArchiveBucket">SourceArchiveBucket</a>: <i>String</i>
    <a href="#sourcearchiveobject" title="SourceArchiveObject">SourceArchiveObject</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#triggerhttp" title="TriggerHttp">TriggerHttp</a>: <i>Boolean</i>
    <a href="#vpcconnector" title="VpcConnector">VpcConnector</a>: <i>String</i>
    <a href="#vpcconnectoregresssettings" title="VpcConnectorEgressSettings">VpcConnectorEgressSettings</a>: <i>String</i>
    <a href="#eventtrigger" title="EventTrigger">EventTrigger</a>: <i>
      - <a href="eventtriggerdefinition.md">EventTriggerDefinition</a></i>
    <a href="#sourcerepository" title="SourceRepository">SourceRepository</a>: <i>
      - <a href="sourcerepositorydefinition.md">SourceRepositoryDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailableMemoryMb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildEnvironmentVariables

_Required_: No

_Type_: List of <a href="buildenvironmentvariablesdefinition.md">BuildEnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryPoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

_Required_: No

_Type_: List of <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsTriggerUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressSettings

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxInstances

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceArchiveBucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceArchiveObject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerHttp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConnector

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConnectorEgressSettings

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventTrigger

_Required_: No

_Type_: List of <a href="eventtriggerdefinition.md">EventTriggerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRepository

_Required_: No

_Type_: List of <a href="sourcerepositorydefinition.md">SourceRepositoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

