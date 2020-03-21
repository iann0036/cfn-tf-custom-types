# Terraform::AWS::OpsworksJavaAppLayer

CloudFormation equivalent of aws_opsworks_java_app_layer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::OpsworksJavaAppLayer",
    "Properties" : {
        "<a href="#appserver" title="AppServer">AppServer</a>" : <i>String</i>,
        "<a href="#appserverversion" title="AppServerVersion">AppServerVersion</a>" : <i>String</i>,
        "<a href="#autoassignelasticips" title="AutoAssignElasticIps">AutoAssignElasticIps</a>" : <i>Boolean</i>,
        "<a href="#autoassignpublicips" title="AutoAssignPublicIps">AutoAssignPublicIps</a>" : <i>Boolean</i>,
        "<a href="#autohealing" title="AutoHealing">AutoHealing</a>" : <i>Boolean</i>,
        "<a href="#customconfigurerecipes" title="CustomConfigureRecipes">CustomConfigureRecipes</a>" : <i>[ String, ... ]</i>,
        "<a href="#customdeployrecipes" title="CustomDeployRecipes">CustomDeployRecipes</a>" : <i>[ String, ... ]</i>,
        "<a href="#custominstanceprofilearn" title="CustomInstanceProfileArn">CustomInstanceProfileArn</a>" : <i>String</i>,
        "<a href="#customjson" title="CustomJson">CustomJson</a>" : <i>String</i>,
        "<a href="#customsecuritygroupids" title="CustomSecurityGroupIds">CustomSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#customsetuprecipes" title="CustomSetupRecipes">CustomSetupRecipes</a>" : <i>[ String, ... ]</i>,
        "<a href="#customshutdownrecipes" title="CustomShutdownRecipes">CustomShutdownRecipes</a>" : <i>[ String, ... ]</i>,
        "<a href="#customundeployrecipes" title="CustomUndeployRecipes">CustomUndeployRecipes</a>" : <i>[ String, ... ]</i>,
        "<a href="#drainelbonshutdown" title="DrainElbOnShutdown">DrainElbOnShutdown</a>" : <i>Boolean</i>,
        "<a href="#elasticloadbalancer" title="ElasticLoadBalancer">ElasticLoadBalancer</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#installupdatesonboot" title="InstallUpdatesOnBoot">InstallUpdatesOnBoot</a>" : <i>Boolean</i>,
        "<a href="#instanceshutdowntimeout" title="InstanceShutdownTimeout">InstanceShutdownTimeout</a>" : <i>Double</i>,
        "<a href="#jvmoptions" title="JvmOptions">JvmOptions</a>" : <i>String</i>,
        "<a href="#jvmtype" title="JvmType">JvmType</a>" : <i>String</i>,
        "<a href="#jvmversion" title="JvmVersion">JvmVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#stackid" title="StackId">StackId</a>" : <i>String</i>,
        "<a href="#systempackages" title="SystemPackages">SystemPackages</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#useebsoptimizedinstances" title="UseEbsOptimizedInstances">UseEbsOptimizedInstances</a>" : <i>Boolean</i>,
        "<a href="#ebsvolume" title="EbsVolume">EbsVolume</a>" : <i>[ <a href="ebsvolume.md">EbsVolume</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::OpsworksJavaAppLayer
Properties:
    <a href="#appserver" title="AppServer">AppServer</a>: <i>String</i>
    <a href="#appserverversion" title="AppServerVersion">AppServerVersion</a>: <i>String</i>
    <a href="#autoassignelasticips" title="AutoAssignElasticIps">AutoAssignElasticIps</a>: <i>Boolean</i>
    <a href="#autoassignpublicips" title="AutoAssignPublicIps">AutoAssignPublicIps</a>: <i>Boolean</i>
    <a href="#autohealing" title="AutoHealing">AutoHealing</a>: <i>Boolean</i>
    <a href="#customconfigurerecipes" title="CustomConfigureRecipes">CustomConfigureRecipes</a>: <i>
      - String</i>
    <a href="#customdeployrecipes" title="CustomDeployRecipes">CustomDeployRecipes</a>: <i>
      - String</i>
    <a href="#custominstanceprofilearn" title="CustomInstanceProfileArn">CustomInstanceProfileArn</a>: <i>String</i>
    <a href="#customjson" title="CustomJson">CustomJson</a>: <i>String</i>
    <a href="#customsecuritygroupids" title="CustomSecurityGroupIds">CustomSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#customsetuprecipes" title="CustomSetupRecipes">CustomSetupRecipes</a>: <i>
      - String</i>
    <a href="#customshutdownrecipes" title="CustomShutdownRecipes">CustomShutdownRecipes</a>: <i>
      - String</i>
    <a href="#customundeployrecipes" title="CustomUndeployRecipes">CustomUndeployRecipes</a>: <i>
      - String</i>
    <a href="#drainelbonshutdown" title="DrainElbOnShutdown">DrainElbOnShutdown</a>: <i>Boolean</i>
    <a href="#elasticloadbalancer" title="ElasticLoadBalancer">ElasticLoadBalancer</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#installupdatesonboot" title="InstallUpdatesOnBoot">InstallUpdatesOnBoot</a>: <i>Boolean</i>
    <a href="#instanceshutdowntimeout" title="InstanceShutdownTimeout">InstanceShutdownTimeout</a>: <i>Double</i>
    <a href="#jvmoptions" title="JvmOptions">JvmOptions</a>: <i>String</i>
    <a href="#jvmtype" title="JvmType">JvmType</a>: <i>String</i>
    <a href="#jvmversion" title="JvmVersion">JvmVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#stackid" title="StackId">StackId</a>: <i>String</i>
    <a href="#systempackages" title="SystemPackages">SystemPackages</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#useebsoptimizedinstances" title="UseEbsOptimizedInstances">UseEbsOptimizedInstances</a>: <i>Boolean</i>
    <a href="#ebsvolume" title="EbsVolume">EbsVolume</a>: <i>
      - <a href="ebsvolume.md">EbsVolume</a></i>
</pre>

## Properties

#### AppServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppServerVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAssignElasticIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAssignPublicIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoHealing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomConfigureRecipes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDeployRecipes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomInstanceProfileArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSetupRecipes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomShutdownRecipes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomUndeployRecipes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrainElbOnShutdown

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticLoadBalancer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallUpdatesOnBoot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceShutdownTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JvmOptions

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JvmType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JvmVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemPackages

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseEbsOptimizedInstances

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsVolume

_Required_: No

_Type_: List of <a href="ebsvolume.md">EbsVolume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

