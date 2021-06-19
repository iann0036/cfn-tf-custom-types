# TF::Aiven::KafkaConnect KafkaConnectUserConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipfilter" title="IpFilter">IpFilter</a>" : <i>[ String, ... ]</i>,
    "<a href="#kafkaconnect" title="KafkaConnect">KafkaConnect</a>" : <i>[ <a href="kafkaconnectdefinition.md">KafkaConnectDefinition</a>, ... ]</i>,
    "<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>" : <i>[ <a href="privateaccessdefinition.md">PrivateAccessDefinition</a>, ... ]</i>,
    "<a href="#privatelinkaccess" title="PrivatelinkAccess">PrivatelinkAccess</a>" : <i>[ <a href="privatelinkaccessdefinition.md">PrivatelinkAccessDefinition</a>, ... ]</i>,
    "<a href="#publicaccess" title="PublicAccess">PublicAccess</a>" : <i>[ <a href="publicaccessdefinition.md">PublicAccessDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipfilter" title="IpFilter">IpFilter</a>: <i>
      - String</i>
<a href="#kafkaconnect" title="KafkaConnect">KafkaConnect</a>: <i>
      - <a href="kafkaconnectdefinition.md">KafkaConnectDefinition</a></i>
<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>: <i>
      - <a href="privateaccessdefinition.md">PrivateAccessDefinition</a></i>
<a href="#privatelinkaccess" title="PrivatelinkAccess">PrivatelinkAccess</a>: <i>
      - <a href="privatelinkaccessdefinition.md">PrivatelinkAccessDefinition</a></i>
<a href="#publicaccess" title="PublicAccess">PublicAccess</a>: <i>
      - <a href="publicaccessdefinition.md">PublicAccessDefinition</a></i>
</pre>

## Properties

#### IpFilter

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaConnect

_Required_: No

_Type_: List of <a href="kafkaconnectdefinition.md">KafkaConnectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateAccess

_Required_: No

_Type_: List of <a href="privateaccessdefinition.md">PrivateAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivatelinkAccess

_Required_: No

_Type_: List of <a href="privatelinkaccessdefinition.md">PrivatelinkAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAccess

_Required_: No

_Type_: List of <a href="publicaccessdefinition.md">PublicAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

