# TF::PrismaCloud::Integration IntegrationConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authtoken" title="AuthToken">AuthToken</a>" : <i>String</i>,
    "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
    "<a href="#hosturl" title="HostUrl">HostUrl</a>" : <i>String</i>,
    "<a href="#integrationkey" title="IntegrationKey">IntegrationKey</a>" : <i>String</i>,
    "<a href="#login" title="Login">Login</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#queueurl" title="QueueUrl">QueueUrl</a>" : <i>String</i>,
    "<a href="#tables" title="Tables">Tables</a>" : <i>[ <a href="tablesdefinition.md">TablesDefinition</a>, ... ]</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authtoken" title="AuthToken">AuthToken</a>: <i>String</i>
<a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
<a href="#hosturl" title="HostUrl">HostUrl</a>: <i>String</i>
<a href="#integrationkey" title="IntegrationKey">IntegrationKey</a>: <i>String</i>
<a href="#login" title="Login">Login</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#queueurl" title="QueueUrl">QueueUrl</a>: <i>String</i>
<a href="#tables" title="Tables">Tables</a>: <i>
      - <a href="tablesdefinition.md">TablesDefinition</a></i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
</pre>

## Properties

#### AuthToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Login

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tables

_Required_: No

_Type_: List of <a href="tablesdefinition.md">TablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

