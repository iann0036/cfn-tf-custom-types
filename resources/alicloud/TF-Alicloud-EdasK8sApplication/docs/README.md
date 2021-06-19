# TF::Alicloud::EdasK8sApplication

CloudFormation equivalent of alicloud_edas_k8s_application

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EdasK8sApplication",
    "Properties" : {
        "<a href="#applicationdescriotion" title="ApplicationDescriotion">ApplicationDescriotion</a>" : <i>String</i>,
        "<a href="#applicationname" title="ApplicationName">ApplicationName</a>" : <i>String</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#command" title="Command">Command</a>" : <i>String</i>,
        "<a href="#commandargs" title="CommandArgs">CommandArgs</a>" : <i>[ String, ... ]</i>,
        "<a href="#edascontainerversion" title="EdasContainerVersion">EdasContainerVersion</a>" : <i>String</i>,
        "<a href="#envs" title="Envs">Envs</a>" : <i>[ <a href="envsdefinition.md">EnvsDefinition</a>, ... ]</i>,
        "<a href="#imageurl" title="ImageUrl">ImageUrl</a>" : <i>String</i>,
        "<a href="#internetslbid" title="InternetSlbId">InternetSlbId</a>" : <i>String</i>,
        "<a href="#internetslbport" title="InternetSlbPort">InternetSlbPort</a>" : <i>Double</i>,
        "<a href="#internetslbprotocol" title="InternetSlbProtocol">InternetSlbProtocol</a>" : <i>String</i>,
        "<a href="#internettargetport" title="InternetTargetPort">InternetTargetPort</a>" : <i>Double</i>,
        "<a href="#jdk" title="Jdk">Jdk</a>" : <i>String</i>,
        "<a href="#limitmcpu" title="LimitMCpu">LimitMCpu</a>" : <i>Double</i>,
        "<a href="#limitmem" title="LimitMem">LimitMem</a>" : <i>Double</i>,
        "<a href="#liveness" title="Liveness">Liveness</a>" : <i>String</i>,
        "<a href="#localvolume" title="LocalVolume">LocalVolume</a>" : <i>String</i>,
        "<a href="#logicalregionid" title="LogicalRegionId">LogicalRegionId</a>" : <i>String</i>,
        "<a href="#mountdescs" title="MountDescs">MountDescs</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#nasid" title="NasId">NasId</a>" : <i>String</i>,
        "<a href="#packagetype" title="PackageType">PackageType</a>" : <i>String</i>,
        "<a href="#packageurl" title="PackageUrl">PackageUrl</a>" : <i>String</i>,
        "<a href="#packageversion" title="PackageVersion">PackageVersion</a>" : <i>String</i>,
        "<a href="#poststart" title="PostStart">PostStart</a>" : <i>String</i>,
        "<a href="#prestop" title="PreStop">PreStop</a>" : <i>String</i>,
        "<a href="#readiness" title="Readiness">Readiness</a>" : <i>String</i>,
        "<a href="#replicas" title="Replicas">Replicas</a>" : <i>Double</i>,
        "<a href="#requestsmcpu" title="RequestsMCpu">RequestsMCpu</a>" : <i>Double</i>,
        "<a href="#requestsmem" title="RequestsMem">RequestsMem</a>" : <i>Double</i>,
        "<a href="#webcontainer" title="WebContainer">WebContainer</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EdasK8sApplication
Properties:
    <a href="#applicationdescriotion" title="ApplicationDescriotion">ApplicationDescriotion</a>: <i>String</i>
    <a href="#applicationname" title="ApplicationName">ApplicationName</a>: <i>String</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#command" title="Command">Command</a>: <i>String</i>
    <a href="#commandargs" title="CommandArgs">CommandArgs</a>: <i>
      - String</i>
    <a href="#edascontainerversion" title="EdasContainerVersion">EdasContainerVersion</a>: <i>String</i>
    <a href="#envs" title="Envs">Envs</a>: <i>
      - <a href="envsdefinition.md">EnvsDefinition</a></i>
    <a href="#imageurl" title="ImageUrl">ImageUrl</a>: <i>String</i>
    <a href="#internetslbid" title="InternetSlbId">InternetSlbId</a>: <i>String</i>
    <a href="#internetslbport" title="InternetSlbPort">InternetSlbPort</a>: <i>Double</i>
    <a href="#internetslbprotocol" title="InternetSlbProtocol">InternetSlbProtocol</a>: <i>String</i>
    <a href="#internettargetport" title="InternetTargetPort">InternetTargetPort</a>: <i>Double</i>
    <a href="#jdk" title="Jdk">Jdk</a>: <i>String</i>
    <a href="#limitmcpu" title="LimitMCpu">LimitMCpu</a>: <i>Double</i>
    <a href="#limitmem" title="LimitMem">LimitMem</a>: <i>Double</i>
    <a href="#liveness" title="Liveness">Liveness</a>: <i>String</i>
    <a href="#localvolume" title="LocalVolume">LocalVolume</a>: <i>String</i>
    <a href="#logicalregionid" title="LogicalRegionId">LogicalRegionId</a>: <i>String</i>
    <a href="#mountdescs" title="MountDescs">MountDescs</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#nasid" title="NasId">NasId</a>: <i>String</i>
    <a href="#packagetype" title="PackageType">PackageType</a>: <i>String</i>
    <a href="#packageurl" title="PackageUrl">PackageUrl</a>: <i>String</i>
    <a href="#packageversion" title="PackageVersion">PackageVersion</a>: <i>String</i>
    <a href="#poststart" title="PostStart">PostStart</a>: <i>String</i>
    <a href="#prestop" title="PreStop">PreStop</a>: <i>String</i>
    <a href="#readiness" title="Readiness">Readiness</a>: <i>String</i>
    <a href="#replicas" title="Replicas">Replicas</a>: <i>Double</i>
    <a href="#requestsmcpu" title="RequestsMCpu">RequestsMCpu</a>: <i>Double</i>
    <a href="#requestsmem" title="RequestsMem">RequestsMem</a>: <i>Double</i>
    <a href="#webcontainer" title="WebContainer">WebContainer</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ApplicationDescriotion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommandArgs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdasContainerVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Envs

_Required_: No

_Type_: List of <a href="envsdefinition.md">EnvsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetSlbId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetSlbPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetSlbProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetTargetPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jdk

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitMCpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitMem

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Liveness

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalVolume

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalRegionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountDescs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NasId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostStart

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreStop

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Readiness

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replicas

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestsMCpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestsMem

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebContainer

_Required_: No

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

