# Terraform::AWS::EmrCluster

CloudFormation equivalent of aws_emr_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EmrCluster",
    "Properties" : {
        "<a href="#additionalinfo" title="AdditionalInfo">AdditionalInfo</a>" : <i>String</i>,
        "<a href="#applications" title="Applications">Applications</a>" : <i>[ String, ... ]</i>,
        "<a href="#autoscalingrole" title="AutoscalingRole">AutoscalingRole</a>" : <i>String</i>,
        "<a href="#configurations" title="Configurations">Configurations</a>" : <i>String</i>,
        "<a href="#configurationsjson" title="ConfigurationsJson">ConfigurationsJson</a>" : <i>String</i>,
        "<a href="#coreinstancecount" title="CoreInstanceCount">CoreInstanceCount</a>" : <i>Double</i>,
        "<a href="#coreinstancetype" title="CoreInstanceType">CoreInstanceType</a>" : <i>String</i>,
        "<a href="#customamiid" title="CustomAmiId">CustomAmiId</a>" : <i>String</i>,
        "<a href="#ebsrootvolumesize" title="EbsRootVolumeSize">EbsRootVolumeSize</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#keepjobflowalivewhennosteps" title="KeepJobFlowAliveWhenNoSteps">KeepJobFlowAliveWhenNoSteps</a>" : <i>Boolean</i>,
        "<a href="#loguri" title="LogUri">LogUri</a>" : <i>String</i>,
        "<a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#releaselabel" title="ReleaseLabel">ReleaseLabel</a>" : <i>String</i>,
        "<a href="#scaledownbehavior" title="ScaleDownBehavior">ScaleDownBehavior</a>" : <i>String</i>,
        "<a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>" : <i>String</i>,
        "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
        "<a href="#step" title="Step">Step</a>" : <i>[ &lt;a href=&#34;step.md&#34;&gt;Step&lt;/a&gt;, ... ]</i>,
        "<a href="#stepconcurrencylevel" title="StepConcurrencyLevel">StepConcurrencyLevel</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#terminationprotection" title="TerminationProtection">TerminationProtection</a>" : <i>Boolean</i>,
        "<a href="#visibletoallusers" title="VisibleToAllUsers">VisibleToAllUsers</a>" : <i>Boolean</i>,
        "<a href="#bootstrapaction" title="BootstrapAction">BootstrapAction</a>" : <i>[ &lt;a href=&#34;bootstrapaction.md&#34;&gt;BootstrapAction&lt;/a&gt;, ... ]</i>,
        "<a href="#coreinstancegroup" title="CoreInstanceGroup">CoreInstanceGroup</a>" : <i>[ &lt;a href=&#34;coreinstancegroup.md&#34;&gt;CoreInstanceGroup&lt;/a&gt;, ... ]</i>,
        "<a href="#ec2attributes" title="Ec2Attributes">Ec2Attributes</a>" : <i>[ &lt;a href=&#34;ec2attributes.md&#34;&gt;Ec2Attributes&lt;/a&gt;, ... ]</i>,
        "<a href="#instancegroup" title="InstanceGroup">InstanceGroup</a>" : <i>[ &lt;a href=&#34;instancegroup.md&#34;&gt;InstanceGroup&lt;/a&gt;, ... ]</i>,
        "<a href="#kerberosattributes" title="KerberosAttributes">KerberosAttributes</a>" : <i>[ &lt;a href=&#34;kerberosattributes.md&#34;&gt;KerberosAttributes&lt;/a&gt;, ... ]</i>,
        "<a href="#masterinstancegroup" title="MasterInstanceGroup">MasterInstanceGroup</a>" : <i>[ &lt;a href=&#34;masterinstancegroup.md&#34;&gt;MasterInstanceGroup&lt;/a&gt;, ... ]</i>,
        "<a href="#ebsconfig" title="EbsConfig">EbsConfig</a>" : <i>[ &lt;a href=&#34;ebsconfig.md&#34;&gt;EbsConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EmrCluster
Properties:
    <a href="#additionalinfo" title="AdditionalInfo">AdditionalInfo</a>: <i>String</i>
    <a href="#applications" title="Applications">Applications</a>: <i>
      - String</i>
    <a href="#autoscalingrole" title="AutoscalingRole">AutoscalingRole</a>: <i>String</i>
    <a href="#configurations" title="Configurations">Configurations</a>: <i>String</i>
    <a href="#configurationsjson" title="ConfigurationsJson">ConfigurationsJson</a>: <i>String</i>
    <a href="#coreinstancecount" title="CoreInstanceCount">CoreInstanceCount</a>: <i>Double</i>
    <a href="#coreinstancetype" title="CoreInstanceType">CoreInstanceType</a>: <i>String</i>
    <a href="#customamiid" title="CustomAmiId">CustomAmiId</a>: <i>String</i>
    <a href="#ebsrootvolumesize" title="EbsRootVolumeSize">EbsRootVolumeSize</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#keepjobflowalivewhennosteps" title="KeepJobFlowAliveWhenNoSteps">KeepJobFlowAliveWhenNoSteps</a>: <i>Boolean</i>
    <a href="#loguri" title="LogUri">LogUri</a>: <i>String</i>
    <a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#releaselabel" title="ReleaseLabel">ReleaseLabel</a>: <i>String</i>
    <a href="#scaledownbehavior" title="ScaleDownBehavior">ScaleDownBehavior</a>: <i>String</i>
    <a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>: <i>String</i>
    <a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
    <a href="#step" title="Step">Step</a>: <i>
      - &lt;a href=&#34;step.md&#34;&gt;Step&lt;/a&gt;</i>
    <a href="#stepconcurrencylevel" title="StepConcurrencyLevel">StepConcurrencyLevel</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#terminationprotection" title="TerminationProtection">TerminationProtection</a>: <i>Boolean</i>
    <a href="#visibletoallusers" title="VisibleToAllUsers">VisibleToAllUsers</a>: <i>Boolean</i>
    <a href="#bootstrapaction" title="BootstrapAction">BootstrapAction</a>: <i>
      - &lt;a href=&#34;bootstrapaction.md&#34;&gt;BootstrapAction&lt;/a&gt;</i>
    <a href="#coreinstancegroup" title="CoreInstanceGroup">CoreInstanceGroup</a>: <i>
      - &lt;a href=&#34;coreinstancegroup.md&#34;&gt;CoreInstanceGroup&lt;/a&gt;</i>
    <a href="#ec2attributes" title="Ec2Attributes">Ec2Attributes</a>: <i>
      - &lt;a href=&#34;ec2attributes.md&#34;&gt;Ec2Attributes&lt;/a&gt;</i>
    <a href="#instancegroup" title="InstanceGroup">InstanceGroup</a>: <i>
      - &lt;a href=&#34;instancegroup.md&#34;&gt;InstanceGroup&lt;/a&gt;</i>
    <a href="#kerberosattributes" title="KerberosAttributes">KerberosAttributes</a>: <i>
      - &lt;a href=&#34;kerberosattributes.md&#34;&gt;KerberosAttributes&lt;/a&gt;</i>
    <a href="#masterinstancegroup" title="MasterInstanceGroup">MasterInstanceGroup</a>: <i>
      - &lt;a href=&#34;masterinstancegroup.md&#34;&gt;MasterInstanceGroup&lt;/a&gt;</i>
    <a href="#ebsconfig" title="EbsConfig">EbsConfig</a>: <i>
      - &lt;a href=&#34;ebsconfig.md&#34;&gt;EbsConfig&lt;/a&gt;</i>
</pre>

## Properties

#### AdditionalInfo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Applications

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configurations

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationsJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreInstanceCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreInstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAmiId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsRootVolumeSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepJobFlowAliveWhenNoSteps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseLabel

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownBehavior

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Step

_Required_: No

_Type_: List of &lt;a href=&#34;step.md&#34;&gt;Step&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepConcurrencyLevel

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationProtection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisibleToAllUsers

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootstrapAction

_Required_: No

_Type_: List of &lt;a href=&#34;bootstrapaction.md&#34;&gt;BootstrapAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreInstanceGroup

_Required_: No

_Type_: List of &lt;a href=&#34;coreinstancegroup.md&#34;&gt;CoreInstanceGroup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2Attributes

_Required_: No

_Type_: List of &lt;a href=&#34;ec2attributes.md&#34;&gt;Ec2Attributes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceGroup

_Required_: No

_Type_: List of &lt;a href=&#34;instancegroup.md&#34;&gt;InstanceGroup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KerberosAttributes

_Required_: No

_Type_: List of &lt;a href=&#34;kerberosattributes.md&#34;&gt;KerberosAttributes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceGroup

_Required_: No

_Type_: List of &lt;a href=&#34;masterinstancegroup.md&#34;&gt;MasterInstanceGroup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsConfig

_Required_: No

_Type_: List of &lt;a href=&#34;ebsconfig.md&#34;&gt;EbsConfig&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### ClusterState

Returns the &lt;code&gt;ClusterState&lt;/code&gt; value.

#### MasterPublicDns

Returns the &lt;code&gt;MasterPublicDns&lt;/code&gt; value.

