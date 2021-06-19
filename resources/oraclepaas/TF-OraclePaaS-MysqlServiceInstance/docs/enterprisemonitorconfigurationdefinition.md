# TF::OraclePaaS::MysqlServiceInstance EnterpriseMonitorConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#emagentpassword" title="EmAgentPassword">EmAgentPassword</a>" : <i>String</i>,
    "<a href="#emagentusername" title="EmAgentUsername">EmAgentUsername</a>" : <i>String</i>,
    "<a href="#empassword" title="EmPassword">EmPassword</a>" : <i>String</i>,
    "<a href="#emport" title="EmPort">EmPort</a>" : <i>Double</i>,
    "<a href="#emusername" title="EmUsername">EmUsername</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#emagentpassword" title="EmAgentPassword">EmAgentPassword</a>: <i>String</i>
<a href="#emagentusername" title="EmAgentUsername">EmAgentUsername</a>: <i>String</i>
<a href="#empassword" title="EmPassword">EmPassword</a>: <i>String</i>
<a href="#emport" title="EmPort">EmPort</a>: <i>Double</i>
<a href="#emusername" title="EmUsername">EmUsername</a>: <i>String</i>
</pre>

## Properties

#### EmAgentPassword

. Password for MySQL Enterprise Monitor agent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmAgentUsername

. Name for the Enterprise Monitor agent user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmPassword

Password for MySQL Enterprise Monitor manager.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmPort

The port number for the MySQL Enterprise Monitor instance. The default is 18443.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmUsername

Name for the Enterprise Monitor Manager user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

