# Terraform::AWS::OpsworksHaproxyLayer

Provides an OpsWorks haproxy layer resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::OpsworksHaproxyLayer",
    "Properties" : {
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
        "<a href="#healthcheckmethod" title="HealthcheckMethod">HealthcheckMethod</a>" : <i>String</i>,
        "<a href="#healthcheckurl" title="HealthcheckUrl">HealthcheckUrl</a>" : <i>String</i>,
        "<a href="#installupdatesonboot" title="InstallUpdatesOnBoot">InstallUpdatesOnBoot</a>" : <i>Boolean</i>,
        "<a href="#instanceshutdowntimeout" title="InstanceShutdownTimeout">InstanceShutdownTimeout</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#stackid" title="StackId">StackId</a>" : <i>String</i>,
        "<a href="#statsenabled" title="StatsEnabled">StatsEnabled</a>" : <i>Boolean</i>,
        "<a href="#statspassword" title="StatsPassword">StatsPassword</a>" : <i>String</i>,
        "<a href="#statsurl" title="StatsUrl">StatsUrl</a>" : <i>String</i>,
        "<a href="#statsuser" title="StatsUser">StatsUser</a>" : <i>String</i>,
        "<a href="#systempackages" title="SystemPackages">SystemPackages</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#useebsoptimizedinstances" title="UseEbsOptimizedInstances">UseEbsOptimizedInstances</a>" : <i>Boolean</i>,
        "<a href="#ebsvolume" title="EbsVolume">EbsVolume</a>" : <i>[ <a href="ebsvolume.md">EbsVolume</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::OpsworksHaproxyLayer
Properties:
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
    <a href="#healthcheckmethod" title="HealthcheckMethod">HealthcheckMethod</a>: <i>String</i>
    <a href="#healthcheckurl" title="HealthcheckUrl">HealthcheckUrl</a>: <i>String</i>
    <a href="#installupdatesonboot" title="InstallUpdatesOnBoot">InstallUpdatesOnBoot</a>: <i>Boolean</i>
    <a href="#instanceshutdowntimeout" title="InstanceShutdownTimeout">InstanceShutdownTimeout</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#stackid" title="StackId">StackId</a>: <i>String</i>
    <a href="#statsenabled" title="StatsEnabled">StatsEnabled</a>: <i>Boolean</i>
    <a href="#statspassword" title="StatsPassword">StatsPassword</a>: <i>String</i>
    <a href="#statsurl" title="StatsUrl">StatsUrl</a>: <i>String</i>
    <a href="#statsuser" title="StatsUser">StatsUser</a>: <i>String</i>
    <a href="#systempackages" title="SystemPackages">SystemPackages</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#useebsoptimizedinstances" title="UseEbsOptimizedInstances">UseEbsOptimizedInstances</a>: <i>Boolean</i>
    <a href="#ebsvolume" title="EbsVolume">EbsVolume</a>: <i>
      - <a href="ebsvolume.md">EbsVolume</a></i>
</pre>

## Properties

#### AutoAssignElasticIps

Whether to automatically assign an elastic IP address to the layer's instances.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAssignPublicIps

For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoHealing

Whether to enable auto-healing for the layer.

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

The ARN of an IAM profile that will be used for the layer's instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomJson

Custom JSON attributes to apply to the layer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSecurityGroupIds

Ids for a set of security groups to apply to the layer's instances.

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

Whether to enable Elastic Load Balancing connection draining.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticLoadBalancer

Name of an Elastic Load Balancer to attach to this layer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckMethod

HTTP method to use for instance healthchecks. Defaults to "OPTIONS".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckUrl

URL path to use for instance healthchecks. Defaults to "/".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallUpdatesOnBoot

Whether to install OS and package updates on each instance when it boots.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceShutdownTimeout

The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A human-readable name for the layer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackId

The id of the stack the layer will belong to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsEnabled

Whether to enable HAProxy stats.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsPassword

The password to use for HAProxy stats.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsUrl

The HAProxy stats URL. Defaults to "/haproxy?stats".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsUser

The username for HAProxy stats. Defaults to "opsworks".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemPackages

Names of a set of system packages to install on the layer's instances.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseEbsOptimizedInstances

Whether to use EBS-optimized instances.

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

#### Id

Returns the <code>Id</code> value.

