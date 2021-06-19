# TF::AWS::ElasticBeanstalkEnvironment

Provides an Elastic Beanstalk Environment Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

Environments are often things such as `development`, `integration`, or
`production`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ElasticBeanstalkEnvironment",
    "Properties" : {
        "<a href="#application" title="Application">Application</a>" : <i>String</i>,
        "<a href="#cnameprefix" title="CnamePrefix">CnamePrefix</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#platformarn" title="PlatformArn">PlatformArn</a>" : <i>String</i>,
        "<a href="#pollinterval" title="PollInterval">PollInterval</a>" : <i>String</i>,
        "<a href="#solutionstackname" title="SolutionStackName">SolutionStackName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
        "<a href="#versionlabel" title="VersionLabel">VersionLabel</a>" : <i>String</i>,
        "<a href="#waitforreadytimeout" title="WaitForReadyTimeout">WaitForReadyTimeout</a>" : <i>String</i>,
        "<a href="#setting" title="Setting">Setting</a>" : <i>[ <a href="settingdefinition.md">SettingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ElasticBeanstalkEnvironment
Properties:
    <a href="#application" title="Application">Application</a>: <i>String</i>
    <a href="#cnameprefix" title="CnamePrefix">CnamePrefix</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#platformarn" title="PlatformArn">PlatformArn</a>: <i>String</i>
    <a href="#pollinterval" title="PollInterval">PollInterval</a>: <i>String</i>
    <a href="#solutionstackname" title="SolutionStackName">SolutionStackName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#tier" title="Tier">Tier</a>: <i>String</i>
    <a href="#versionlabel" title="VersionLabel">VersionLabel</a>: <i>String</i>
    <a href="#waitforreadytimeout" title="WaitForReadyTimeout">WaitForReadyTimeout</a>: <i>String</i>
    <a href="#setting" title="Setting">Setting</a>: <i>
      - <a href="settingdefinition.md">SettingDefinition</a></i>
</pre>

## Properties

#### Application

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CnamePrefix

Prefix to use for the fully qualified DNS name of
the Environment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Short description of the Environment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for this Environment. This name is used
in the application URL.

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

A set of tags to apply to the Environment. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionLabel

The name of the Elastic Beanstalk Application Version
to use in deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForReadyTimeout

The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Setting

_Required_: No

_Type_: List of <a href="settingdefinition.md">SettingDefinition</a>

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

Returns the <code>AllSettings</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### AutoscalingGroups

Returns the <code>AutoscalingGroups</code> value.

#### Cname

Returns the <code>Cname</code> value.

#### EndpointUrl

Returns the <code>EndpointUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### Instances

Returns the <code>Instances</code> value.

#### LaunchConfigurations

Returns the <code>LaunchConfigurations</code> value.

#### LoadBalancers

Returns the <code>LoadBalancers</code> value.

#### Queues

Returns the <code>Queues</code> value.

#### Triggers

Returns the <code>Triggers</code> value.

