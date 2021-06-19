# TF::GoogleBeta::GoogleAppEngineStandardAppVersion

CloudFormation equivalent of google_app_engine_standard_app_version

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleAppEngineStandardAppVersion",
    "Properties" : {
        "<a href="#deleteserviceondestroy" title="DeleteServiceOnDestroy">DeleteServiceOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#envvariables" title="EnvVariables">EnvVariables</a>" : <i>[ <a href="envvariablesdefinition.md">EnvVariablesDefinition</a>, ... ]</i>,
        "<a href="#inboundservices" title="InboundServices">InboundServices</a>" : <i>[ String, ... ]</i>,
        "<a href="#instanceclass" title="InstanceClass">InstanceClass</a>" : <i>String</i>,
        "<a href="#noopondestroy" title="NoopOnDestroy">NoopOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#runtimeapiversion" title="RuntimeApiVersion">RuntimeApiVersion</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#threadsafe" title="Threadsafe">Threadsafe</a>" : <i>Boolean</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>,
        "<a href="#automaticscaling" title="AutomaticScaling">AutomaticScaling</a>" : <i>[ <a href="automaticscalingdefinition.md">AutomaticScalingDefinition</a>, ... ]</i>,
        "<a href="#basicscaling" title="BasicScaling">BasicScaling</a>" : <i>[ <a href="basicscalingdefinition.md">BasicScalingDefinition</a>, ... ]</i>,
        "<a href="#deployment" title="Deployment">Deployment</a>" : <i>[ <a href="deploymentdefinition.md">DeploymentDefinition</a>, ... ]</i>,
        "<a href="#entrypoint" title="Entrypoint">Entrypoint</a>" : <i>[ <a href="entrypointdefinition.md">EntrypointDefinition</a>, ... ]</i>,
        "<a href="#handlers" title="Handlers">Handlers</a>" : <i>[ <a href="handlersdefinition.md">HandlersDefinition</a>, ... ]</i>,
        "<a href="#libraries" title="Libraries">Libraries</a>" : <i>[ <a href="librariesdefinition.md">LibrariesDefinition</a>, ... ]</i>,
        "<a href="#manualscaling" title="ManualScaling">ManualScaling</a>" : <i>[ <a href="manualscalingdefinition.md">ManualScalingDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#vpcaccessconnector" title="VpcAccessConnector">VpcAccessConnector</a>" : <i>[ <a href="vpcaccessconnectordefinition.md">VpcAccessConnectorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleAppEngineStandardAppVersion
Properties:
    <a href="#deleteserviceondestroy" title="DeleteServiceOnDestroy">DeleteServiceOnDestroy</a>: <i>Boolean</i>
    <a href="#envvariables" title="EnvVariables">EnvVariables</a>: <i>
      - <a href="envvariablesdefinition.md">EnvVariablesDefinition</a></i>
    <a href="#inboundservices" title="InboundServices">InboundServices</a>: <i>
      - String</i>
    <a href="#instanceclass" title="InstanceClass">InstanceClass</a>: <i>String</i>
    <a href="#noopondestroy" title="NoopOnDestroy">NoopOnDestroy</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#runtimeapiversion" title="RuntimeApiVersion">RuntimeApiVersion</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#threadsafe" title="Threadsafe">Threadsafe</a>: <i>Boolean</i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
    <a href="#automaticscaling" title="AutomaticScaling">AutomaticScaling</a>: <i>
      - <a href="automaticscalingdefinition.md">AutomaticScalingDefinition</a></i>
    <a href="#basicscaling" title="BasicScaling">BasicScaling</a>: <i>
      - <a href="basicscalingdefinition.md">BasicScalingDefinition</a></i>
    <a href="#deployment" title="Deployment">Deployment</a>: <i>
      - <a href="deploymentdefinition.md">DeploymentDefinition</a></i>
    <a href="#entrypoint" title="Entrypoint">Entrypoint</a>: <i>
      - <a href="entrypointdefinition.md">EntrypointDefinition</a></i>
    <a href="#handlers" title="Handlers">Handlers</a>: <i>
      - <a href="handlersdefinition.md">HandlersDefinition</a></i>
    <a href="#libraries" title="Libraries">Libraries</a>: <i>
      - <a href="librariesdefinition.md">LibrariesDefinition</a></i>
    <a href="#manualscaling" title="ManualScaling">ManualScaling</a>: <i>
      - <a href="manualscalingdefinition.md">ManualScalingDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#vpcaccessconnector" title="VpcAccessConnector">VpcAccessConnector</a>: <i>
      - <a href="vpcaccessconnectordefinition.md">VpcAccessConnectorDefinition</a></i>
</pre>

## Properties

#### DeleteServiceOnDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvVariables

_Required_: No

_Type_: List of <a href="envvariablesdefinition.md">EnvVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundServices

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoopOnDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeApiVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threadsafe

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticScaling

_Required_: No

_Type_: List of <a href="automaticscalingdefinition.md">AutomaticScalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicScaling

_Required_: No

_Type_: List of <a href="basicscalingdefinition.md">BasicScalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deployment

_Required_: No

_Type_: List of <a href="deploymentdefinition.md">DeploymentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entrypoint

_Required_: No

_Type_: List of <a href="entrypointdefinition.md">EntrypointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handlers

_Required_: No

_Type_: List of <a href="handlersdefinition.md">HandlersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Libraries

_Required_: No

_Type_: List of <a href="librariesdefinition.md">LibrariesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualScaling

_Required_: No

_Type_: List of <a href="manualscalingdefinition.md">ManualScalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcAccessConnector

_Required_: No

_Type_: List of <a href="vpcaccessconnectordefinition.md">VpcAccessConnectorDefinition</a>

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

#### Name

Returns the <code>Name</code> value.

