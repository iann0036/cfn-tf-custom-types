# Terraform::AWS::ElasticBeanstalkEnvironment

CloudFormation equivalent of aws_elastic_beanstalk_environment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ElasticBeanstalkEnvironment",
    "Properties" : {
        "<a href="#application" title="Application">Application</a>" : <i>String</i>,
        "<a href="#cnameprefix" title="CnamePrefix">CnamePrefix</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#platformarn" title="PlatformArn">PlatformArn</a>" : <i>String</i>,
        "<a href="#pollinterval" title="PollInterval">PollInterval</a>" : <i>String</i>,
        "<a href="#solutionstackname" title="SolutionStackName">SolutionStackName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
        "<a href="#versionlabel" title="VersionLabel">VersionLabel</a>" : <i>String</i>,
        "<a href="#waitforreadytimeout" title="WaitForReadyTimeout">WaitForReadyTimeout</a>" : <i>String</i>,
        "<a href="#setting" title="Setting">Setting</a>" : <i>[ &lt;a href=&#34;setting.md&#34;&gt;Setting&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ElasticBeanstalkEnvironment
Properties:
    <a href="#application" title="Application">Application</a>: <i>String</i>
    <a href="#cnameprefix" title="CnamePrefix">CnamePrefix</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#platformarn" title="PlatformArn">PlatformArn</a>: <i>String</i>
    <a href="#pollinterval" title="PollInterval">PollInterval</a>: <i>String</i>
    <a href="#solutionstackname" title="SolutionStackName">SolutionStackName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#tier" title="Tier">Tier</a>: <i>String</i>
    <a href="#versionlabel" title="VersionLabel">VersionLabel</a>: <i>String</i>
    <a href="#waitforreadytimeout" title="WaitForReadyTimeout">WaitForReadyTimeout</a>: <i>String</i>
    <a href="#setting" title="Setting">Setting</a>: <i>
      - &lt;a href=&#34;setting.md&#34;&gt;Setting&lt;/a&gt;</i>
</pre>

## Properties

#### Application

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CnamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PollInterval

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SolutionStackName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForReadyTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Setting

_Required_: No

_Type_: List of &lt;a href=&#34;setting.md&#34;&gt;Setting&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllSettings

Returns the &lt;code&gt;AllSettings&lt;/code&gt; value.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### AutoscalingGroups

Returns the &lt;code&gt;AutoscalingGroups&lt;/code&gt; value.

#### Cname

Returns the &lt;code&gt;Cname&lt;/code&gt; value.

#### EndpointUrl

Returns the &lt;code&gt;EndpointUrl&lt;/code&gt; value.

#### Instances

Returns the &lt;code&gt;Instances&lt;/code&gt; value.

#### LaunchConfigurations

Returns the &lt;code&gt;LaunchConfigurations&lt;/code&gt; value.

#### LoadBalancers

Returns the &lt;code&gt;LoadBalancers&lt;/code&gt; value.

#### Queues

Returns the &lt;code&gt;Queues&lt;/code&gt; value.

#### Triggers

Returns the &lt;code&gt;Triggers&lt;/code&gt; value.

