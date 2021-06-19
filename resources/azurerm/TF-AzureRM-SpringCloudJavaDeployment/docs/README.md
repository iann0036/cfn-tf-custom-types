# TF::AzureRM::SpringCloudJavaDeployment

Manages an Azure Spring Cloud Deployment with a Java runtime.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SpringCloudJavaDeployment",
    "Properties" : {
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
        "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>, ... ]</i>,
        "<a href="#instancecount" title="InstanceCount">InstanceCount</a>" : <i>Double</i>,
        "<a href="#jvmoptions" title="JvmOptions">JvmOptions</a>" : <i>String</i>,
        "<a href="#memoryingb" title="MemoryInGb">MemoryInGb</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#runtimeversion" title="RuntimeVersion">RuntimeVersion</a>" : <i>String</i>,
        "<a href="#springcloudappid" title="SpringCloudAppId">SpringCloudAppId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SpringCloudJavaDeployment
Properties:
    <a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
    <a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a></i>
    <a href="#instancecount" title="InstanceCount">InstanceCount</a>: <i>Double</i>
    <a href="#jvmoptions" title="JvmOptions">JvmOptions</a>: <i>String</i>
    <a href="#memoryingb" title="MemoryInGb">MemoryInGb</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#runtimeversion" title="RuntimeVersion">RuntimeVersion</a>: <i>String</i>
    <a href="#springcloudappid" title="SpringCloudAppId">SpringCloudAppId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Cpu

Specifies the required cpu of the Spring Cloud Deployment. Possible Values are between `1` and `4`. Defaults to `1` if not specified.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

Specifies the environment variables of the Spring Cloud Deployment as a map of key-value pairs.

_Required_: No

_Type_: List of <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCount

Specifies the required instance count of the Spring Cloud Deployment. Possible Values are between `1` and `500`. Defaults to `1` if not specified.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JvmOptions

Specifies the jvm option of the Spring Cloud Deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryInGb

Specifies the required memory size of the Spring Cloud Deployment. Possible Values are between `1` and `8`. Defaults to `1` if not specified.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Spring Cloud Deployment. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeVersion

Specifies the runtime version of the Spring Cloud Deployment. Possible Values are `Java_8` and `Java_11`. Defaults to `Java_8`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpringCloudAppId

Specifies the id of the Spring Cloud Application in which to create the Deployment. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

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

