# TF::Aiven::Cassandra CassandraUserConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipfilter" title="IpFilter">IpFilter</a>" : <i>[ String, ... ]</i>,
    "<a href="#migratesstableloader" title="MigrateSstableloader">MigrateSstableloader</a>" : <i>String</i>,
    "<a href="#projecttoforkfrom" title="ProjectToForkFrom">ProjectToForkFrom</a>" : <i>String</i>,
    "<a href="#servicetoforkfrom" title="ServiceToForkFrom">ServiceToForkFrom</a>" : <i>String</i>,
    "<a href="#cassandra" title="Cassandra">Cassandra</a>" : <i>[ <a href="cassandradefinition.md">CassandraDefinition</a>, ... ]</i>,
    "<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>" : <i>[ <a href="privateaccessdefinition.md">PrivateAccessDefinition</a>, ... ]</i>,
    "<a href="#publicaccess" title="PublicAccess">PublicAccess</a>" : <i>[ <a href="publicaccessdefinition.md">PublicAccessDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipfilter" title="IpFilter">IpFilter</a>: <i>
      - String</i>
<a href="#migratesstableloader" title="MigrateSstableloader">MigrateSstableloader</a>: <i>String</i>
<a href="#projecttoforkfrom" title="ProjectToForkFrom">ProjectToForkFrom</a>: <i>String</i>
<a href="#servicetoforkfrom" title="ServiceToForkFrom">ServiceToForkFrom</a>: <i>String</i>
<a href="#cassandra" title="Cassandra">Cassandra</a>: <i>
      - <a href="cassandradefinition.md">CassandraDefinition</a></i>
<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>: <i>
      - <a href="privateaccessdefinition.md">PrivateAccessDefinition</a></i>
<a href="#publicaccess" title="PublicAccess">PublicAccess</a>: <i>
      - <a href="publicaccessdefinition.md">PublicAccessDefinition</a></i>
</pre>

## Properties

#### IpFilter

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MigrateSstableloader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectToForkFrom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceToForkFrom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cassandra

_Required_: No

_Type_: List of <a href="cassandradefinition.md">CassandraDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateAccess

_Required_: No

_Type_: List of <a href="privateaccessdefinition.md">PrivateAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAccess

_Required_: No

_Type_: List of <a href="publicaccessdefinition.md">PublicAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

